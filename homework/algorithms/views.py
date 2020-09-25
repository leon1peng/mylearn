from django.shortcuts import render
from django.views.generic.base import View
from .models import HomeworkInfo
from datetime import datetime
from django.http import JsonResponse


# Create your views here.
def index(request):
    homeworks = HomeworkInfo.objects.all()
    # homeworks = [{"homeworkId": 1, "username": "Leon", "number": 77, "topicName": "爬楼梯", "difficulty": "简单",
    #               "times": 1, "comment": ""}]
    return render(request, "algorithms/index.html", {"homeworks": homeworks})


def homework(request):
    username = request.POST.get("username")
    number = request.POST.get("number")
    topic_name = request.POST.get("topicName")
    difficulty = request.POST.get("difficulty")

    recording = [[], [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]]
    HomeworkInfo.objects.create(username=username, number=number, topicName=topic_name, difficulty=difficulty,
                                recording=recording)

    return JsonResponse({'res': 1})


def add(request):
    return render(request, "algorithms/add.html")


class Detail(View):
    def get(self, request, homework_id):
        print(request.method)
        homework_obj = HomeworkInfo.objects.filter(homeworkId=homework_id).first()
        return render(request, "algorithms/detail.html", {"homework": homework_obj})


def update_time_comment(request):
    update_obj = HomeworkInfo.objects.filter(homeworkId=request.POST.get("homeworkId")).first()
    update_obj.times = int(request.POST.get("times"))
    update_obj.comment = request.POST.get("comment")
    update_obj.save()
    return JsonResponse({'res': 1})
