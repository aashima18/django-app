from django.urls import path
from django.conf.urls import url
from .import views
from .views import start,start_quiz,question_view,logout,submit_quiz


urlpatterns = [
     path('',views.start,name='start'),
     path('startt/',views.start_quiz,name='startt'),
     path('questions/',views.question_view,name='questions'),
     path('logout',views.logout,name='logout'),
     path('answers/',views.submit_quiz,name='answers'),
     


]