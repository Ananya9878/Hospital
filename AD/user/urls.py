from django.urls import path,include
from . import views


urlpatterns = [
    path('signup/',views.sign_up),
    path('login/',views.log_in),
    path('logout/',views.log_out),

]
