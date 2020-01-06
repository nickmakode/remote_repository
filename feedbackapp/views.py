from django.shortcuts import render
from feedbackapp.models import FeedbackData
from feedbackapp.forms import FeedbackForm
from django.http import HttpResponse
from datetime import datetime as dt
x=dt.now()

def feedbackview(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get("name")
            rating1=request.POST.get("rating")
            feedback1=request.POST.get("feedback")

            data=FeedbackData(
                name=name1,\
                rating=rating1,
                feedback=feedback1,
            )
            data.save()

            fform=FeedbackForm()
            feedbacks=FeedbackData.objects.all()

            return render(request,'feedback.html',{'abcd':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse("<h1>Please Enter Your Details...</h1>")
    else:
        fform=FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request, 'feedback.html', {'abcd': fform, 'feedbacks': feedbacks})




