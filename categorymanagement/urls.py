from django.urls import path
from .import views
from .views import categorym,categorys,success,parentt



urlpatterns=[
     path('',views.categorym,name='category'),
     path('categorys/',views.categorys,name='categorys'),
     path('success/',views.success,name='success'),
     path('parentt/<int:id>',views.parentt,name='parentt'),


]