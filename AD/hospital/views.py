from django.shortcuts import render,HttpResponse
from .models import Hospital,Department,HospitalImage,DepartmentImage,MessageModel
from doctor.models import Doctor
from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models import Q
# Create your views here.

def home(request):
    hospitals = Hospital.objects.all()
    context = {"hospitals" : hospitals,"MEDIA_URL":settings.MEDIA_URL
    }
    user = request.user
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request,'hospital/home.html',context=context)

def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        description = request.POST.get("description")
        no_of_doctors = request.POST.get("no_of_doctors")
        no_of_beds = request.POST.get("no_of_beds")
        h = Hospital.objects.create(name=name,
                                    address=address,
                                    description=description,
                                    no_of_doctors=no_of_doctors,
                                    no_of_beds=no_of_beds)
        h.save()
        return HttpResponse('Hospital added')
    else:
        return render(request,'hospital/add_doctor.html')

def delete(request,id):
    hospital = Hospital.objects.get(id=id)
    hospital.delete()
    return HttpResponse('deleted')

def update(request,id):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        description = request.POST.get("description")
        no_of_doctors = request.POST.get("no_of_doctors")
        no_of_beds = request.POST.get("no_of_beds")
        hospital = Hospital.objects.filter(id=id)
        hospital.update(name=name,address=address,
                        description=description,
                        no_of_doctors=no_of_doctors,
                        no_of_beds=no_of_beds)
        return HttpResponse('Hospital Updated')
    else:
        hospital = Hospital.objects.get(id=id)
        context = {"hospital": hospital}
        return render(request,'hospital/update_hospital.html',context)

def get(request,id):
    hospital = Hospital.objects.get(id=id)
    department = Department.objects.filter(hospital=id)
    doctor = Doctor.objects.filter(hospital=id)
    hospital_image = HospitalImage.objects.filter(hospital=id)
    context = {"hospital":hospital,"department":department,'doctor':doctor,
               "MEDIA_URL":settings.MEDIA_URL,"hospital_image":hospital_image}
    user = request.user
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request,'hospital/hospital_detail.html',context)

def get_list(request):
    all_hospital = Hospital.objects.all()
    context = {'hospitals':all_hospital}
    return render(request,'hospital/hospital_list.html',context)

def department(request,id):
    department = Department.objects.get(id=id)
    doctor = Doctor.objects.filter(department=id)
    hospital = department.hospital
    department_image = DepartmentImage.objects.filter(department=id)
    # hospital = Hospital.objects.get(id=hospital_id)
    context = {"department":department,'doctor':doctor,
               "hospital":hospital,"MEDIA_URL":settings.MEDIA_URL}
    user = request.user
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request,'hospital/department_details.html',context)

def search(request):
    if request.method == 'GET':
        query_parameter = request.GET.get("search")
        state = request.GET.get("state")
        district = request.GET.get("district")
        try:
            if state == "SelectState":
                lookup = (Q(name__icontains=query_parameter) | Q(address__icontains=query_parameter)
                            | Q(department__name=query_parameter) | Q(description__icontains=query_parameter))
            else:

                lookup = Q(state=state)&Q(district=district)&(Q(name__icontains=query_parameter)|Q(address__icontains=query_parameter)\
                         |Q(department__name=query_parameter)|Q(description__icontains=query_parameter))
            hospitals = Hospital.objects.filter(lookup).distinct()

        except:
            hospitals = {}
        context = {"hospitals": hospitals, "MEDIA_URL": settings.MEDIA_URL
                   }
        user = request.user
        if user.username == 'AnonymousUser':
            context['user'] = ''
        else:
            context['user'] = user.username
        return render(request, 'hospital/home.html', context=context)
    else:
        return render(request, 'hospital/home.html',{})


def message(request,id):
    if request.method == 'POST':
        user = request.user
        hospital = id
        message = request.POST.get("message")
        # isSenderUser = request.POST.get("isSenderUser")
        # if user:
        #     user = User.objects.get(pk=user)
        if hospital:
            hospital = Hospital.objects.get(pk=hospital)
        d = MessageModel.objects.create(user=user,hospital=hospital,
                                        message=message,isSenderUser=True)
        d.save()
        return redirect(request.path_info)

    else:
        user = request.user
        all_message = MessageModel.objects.filter(hospital=id,user=user.id)
        context = {'all_message':all_message}
        # return HttpResponse(all_message)
        return render(request,'hospital/message_page.html',context=context)




