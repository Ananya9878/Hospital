from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('<int:id>',views.get),
    path('update/<int:id>',views.update),
    path('add/',views.add),
    path('delete/<int:id>',views.delete),
    path('get_list/',views.get_list),
    path('department/<int:id>',views.department),
    path('search',views.search),
    path('<int:id>/message',views.message),


]
