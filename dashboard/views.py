from django.shortcuts import render,redirect
from frontend.models import Course

def dashboard(request):
    return render(request,"dashboard/dashboard.html") 


def course_view(request):
    courses=Course.objects.all()
    context={
        "courses":courses
    }
    return render(request,"dashboard/course.html",context)

def course_add(request):
    try:
        if request.method=="POST":
            name=request.POST.get("name")
            duration=request.POST.get("duration")
            c=Course.objects.create(
                name=name,
                duration=duration
            )
    except Exception as e:
        print(e)
    return redirect('course_view')

def course_update(request):
    pass

def course_delete(request):
    if request.method=="POST":
        id=request.POST.get("courseid")
        course=Course.objects.filter(id=id).first()
        course.delete()
    return redirect('course_view')

