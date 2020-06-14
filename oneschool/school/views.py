from django.shortcuts import render

# Create your views here.

def single(request):
    data = {

    }
    return render(request, 'course-single.html', data)
