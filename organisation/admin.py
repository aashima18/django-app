from django.contrib import admin
from organisation.models import  Organisation, Courses,Student
# Register your models here.
# admin.site.register(Organisation)
@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name',)


# admin.site.register(Courses)
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('courses','organisation','name')