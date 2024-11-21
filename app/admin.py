from django.contrib import admin
from .models import Student
admin.site.site_header="siplaya info tech"
admin.site.index_title="courses"

# Register your models here.
@admin.register(Student)
class CourseAdmin(admin.ModelAdmin):
    list_display=["id","name","email","contact","message"]

