from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader #loader
from django.shortcuts import render,get_object_or_404

from django.urls import reverse
from django.views import generic

from .models import Question,Choice



# from django.http import Http404

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html") load the template 
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     # return HttpResponse(template.render(context, request)) return HttpResponse with the result of the rendered tempalte
#     return render(request, "polls/index.html", context)

# def detail (request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html",{"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
#
# old views

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# We’re using two generic views here: ListView and DetailView. 
# Respectively, those two views abstract the concepts of “display a list of objects” 
# and “display a detail page for a particular type of object.”

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question_id,)))

