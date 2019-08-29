from django.urls import path
from . import views
from .views import StudentListView,StudentCreateView,load_courses,courses, OCreateView,OListView,cou, SearchResultsView,org,successs,SearchResultsView1,SearchResultsView2
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search1/', SearchResultsView1.as_view(), name='search1_results'),
    path('search2/', SearchResultsView2.as_view(), name='search2_results'),
    path('', views. OCreateView.as_view(), name='organise'),
    path('addd/', views.OListView.as_view(), name='otlist'),
    path('cou/<int:organisation_id>',views.cou,name='cou'),
    path('success/',views.success,name='success'),
    path('org/<int:organisation_id>',views.org,name='org'),
    path('stu/<int:courses_id>/<int:organisation_id>',views.stu,name='stu'),
    path('successs/',views.successs,name='successs'),

    path('add/', views.StudentListView.as_view(), name='stlist'),
    path('create/', views.StudentCreateView.as_view(), name='add'),
    path('lcourses/', views.load_courses, name='load_courses'),
    path('courses/<int:id>',views.courses,name='courses'),
    path('organi/<int:id>',views.organi,name='organi'),
   
]