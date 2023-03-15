
from django.urls import path
from . import views


urlpatterns = [
    path('hello', views.Hello),
    path('addDept',views.addDept),
    path('saveDept',views.saveDept),
]