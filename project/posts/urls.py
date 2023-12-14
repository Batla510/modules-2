from django.urls import path
from .views import index,delete,post,create,update

urlpatterns = [
    path('',index,name='home'),
    path('delete/<int:id>',delete,name='delete'),
    path('post/<int:id>',post,name='post'),
    path('create',create,name='create'),
    path('update/<int:id>',update,name='update'),
]