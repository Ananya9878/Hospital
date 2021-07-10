from django.shortcuts import render,HttpResponse
from .models import Doctor
from django.conf import settings
from django.db.models import Q

# Create your views here.
def home(request):
    doctor = Doctor.objects.all()
    context = {"doctor": doctor, "MEDIA_URL": settings.MEDIA_URL
               }
    user = request.user
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request, 'doctor/home.html', context=context)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        degree = request.POST.get('degree')
        years_of_experience = request.POST.get('years_of_experience')
        hospital_name = request.POST.get('hospital_name')
        d = Doctor.objects.create(name=name,
                                  designation=designation,
                                  degree=degree,
                                  years_of_experience=years_of_experience,
                                  hospital_name=hospital_name)

        d.save()
        return HttpResponse('Doctor added')
    else:
        return render(request,'add_doctor.html')

def delete(request):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return HttpResponse('deleted')

def update(request):
    if request.method == 'GET':
        doctor = Doctor.objects.get(id=id)
        context = {"doctor": doctor}
        return render(request,'update_doctor.html',context)
    return HttpResponse('update_hospital_working')

def get(request,id):
    doctor = Doctor.objects.get(id=id)
    context = {"doctor": doctor}
    user = request.user
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request, 'doctor/doctor_detail.html', context)

def get_list(request):
    all_doctors = Doctor.objects.all()
    context = {'doctors':all_doctors}
    user = request.user
    if user.username == 'AnonymousUser':
        context['user'] = ''
    else:
        context['user'] = user.username
    return render(request,'doctor_list.html',context)

def search(request):
    if request.method == 'GET':
        query_parameter = request.GET.get("search")
        state = request.GET.get("state")
        district = request.GET.get("district")
        try:
            if state == "SelectState":
                lookup = Q(name__icontains=query_parameter) | Q(hospital__address__icontains=query_parameter) \
                         | Q(degree__icontains=query_parameter) \
                         | Q(designation__icontains=query_parameter) \
                         | Q(department__name__icontains=query_parameter)
            else:
                lookup = Q(hospital__state=state)&Q(hospital__district=district)&(Q(name__icontains=query_parameter)|Q(hospital__address__icontains=query_parameter)\
                         |Q(degree__icontains=query_parameter)\
                         |Q(designation__icontains=query_parameter)\
                         |Q(department__name__icontains=query_parameter))
            doctor = Doctor.objects.filter(lookup).distinct()

        except:
            doctor = {}
        context = {"doctor": doctor, "MEDIA_URL": settings.MEDIA_URL
                   }
        user = request.user
        if user.username == 'AnonymousUser':
            context['user'] = ''
        else:
            context['user'] = user.username
        return render(request, 'doctor/home.html', context=context)
    else:
        return render(request, 'doctor/home.html',{})


