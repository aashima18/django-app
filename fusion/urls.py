from django.urls import path
from django.conf.urls import url
from .import views
from .views import indexx,feedback,signup

urlpatterns=[
    path('',views.indexx,name='indexx'),
    path('feedback/',views.feedback,name='feedback'),
    
    path('signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    

]