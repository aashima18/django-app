from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Student, Courses,Organisation
from .forms import StudentForm, OrganisationForm,CoursesForm
from django.db.models import Q




# addorganisation---------------------------------------------------------
class OCreateView(CreateView):
    model = Organisation
    form_class = OrganisationForm
    success_url = reverse_lazy('otlist')    


class OListView(ListView):
    model = Organisation
    context_object_name = 'org'
    queryset = Organisation.objects.order_by('name')
    template_name = 'organisation/organisation_list.html ' 


class SearchResultsView(ListView):
    model = Organisation
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Organisation.objects.filter(Q(name__icontains=query)).order_by('name')
        return object_list    


# addcourse---------------------------------------------------------


def cou(request,organisation_id):
    if request.method == 'POST':
        form = CoursesForm(request.POST)   

        if form.is_valid():
          a = form.save(commit=False)
          a.name = form.cleaned_data['name']
          a.organisation = Organisation.objects.get(pk = organisation_id)
          
        #   Courses.objects.create(name=name,organisation=a.organisation)
          a.save()
          return HttpResponseRedirect(reverse('success'))
          
    else:
        form = CoursesForm(request.POST)  
    return render(request, "organisation/courses_form.html", {'form': form})


def success(request):
    data=Courses.objects.all()
    data=Courses.objects.order_by('name')
    context = {
            'data':data 
    }
    return render(request,'coursel.html',context=context)

class SearchResultsView1(ListView):
    model = Courses
    template_name = 'search1_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Courses.objects.filter(Q(name__icontains=query)).order_by('name')
        return object_list    



def org(request,organisation_id):
    dataa=Courses.objects.filter(id=organisation_id)
    
    context = {
            'dataa':dataa 
    }
    return render(request,'orgl.html',context=context)


#addstudent----------------------------


def stu(request,courses_id,organisation_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)      
        # print(form.is_valid())
        if form.is_valid():
          a = form.save()
          a.name = form.cleaned_data['name']
          
          a.courses = Courses.objects.get(pk = courses_id)
          a.organisation = Organisation.objects.get(pk = organisation_id)
          a.save()
        #   Student.objects.create(name=name,courses=a.courses,organisation=a.organisation)
          return HttpResponseRedirect(reverse('successs'))
    else:
        form = StudentForm(request.POST)  
    return render(request, "organisation/courses_form.html", {'form': form})


def successs(request):
    dta=Student.objects.all()
    dta = Student.objects.order_by('name')
    context = {
            'dta':dta 
    }
    return render(request,'sl.html',context=context)


class SearchResultsView2(ListView):
    model = Student
    template_name = 'search2_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Student.objects.filter(Q(name__icontains=query)|Q(courses__name__icontains=query)|Q(organisation__name__icontains=query)).order_by('name')
        return object_list 





















































# addstudent---------------------------------------------------------------

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('stlist')  
   


def load_courses(request):
    organisation_id = request.GET.get('organisation')
    courses = Courses.objects.filter(organisation_id=organisation_id).order_by('name')
    return render(request, 'organisation/courses.html', {'courses': courses})    



class StudentListView(ListView):
    model = Student
    context_object_name = 'people'
    template_name = 'organisation/student_list.html ' 



def courses(request,id):    
    dataa = Student.objects.filter(id=id)
    return render(request,'cour.html',{'dataa': dataa})


def organi(request,id):    
    item = Student.objects.filter(id=id)
    return render(request,'org.html',{'item': item})
























