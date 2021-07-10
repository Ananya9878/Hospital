
from django.contrib import admin
from .models import Hospital,Department,DepartmentImage,HospitalImage,MessageModel

class HospitalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hospital, HospitalAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class HospitalImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(HospitalImage,HospitalImageAdmin)

class DepartmentImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(DepartmentImage,DepartmentImageAdmin)

class MessageModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(MessageModel,MessageModelAdmin)
