from xml.etree.ElementInclude import include
from django.urls import path, re_path, include
from myApp import views
from myApp.iris.views import irisData, insertData, updateData, deleteData

urlpatterns = [
    re_path(r'^home/', views.home, name='home'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('iris/', irisData, name='iris'),
    path('insertData/', insertData, name='insertData'),
    path('updateData/', updateData, name='updateData'),
    path('deleteData/', deleteData, name='deleteData'),

]
