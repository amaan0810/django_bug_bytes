from django.db.models import F
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice

from django.views import generic




class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name="lastest_questions"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['numbers']=[1,2,3,4,5]
        return context

# Create your views here.
def index(request):
 
    lastest_questions=Question.objects.order_by("pub_date")[:5]
    # result=", \n".join([q.question_text for q in lastest_questions])

    # template=loader.get_template("polls/index.html")
    # context={ 
    #     "lastest_questions": lastest_questions
    # }
    # return HttpResponse(template.render(context,request))

    context={ 
        "lastest_questions": lastest_questions
    }

    return render(request,"polls/index.html",context)



class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detial.html"


def detail(request,question_id):
    # try: 
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Questions not Found")
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detial.html",{"question": question})



def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    print(request.POST)
    try: 
        choice_id=request.POST["choice"]
        selected_choice=question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist): 
        return render(request,"polls/detial.html",context={
            "question": question,
            "error_message": "You didn't select a choice.",

        })
    else : 
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class ResultView(generic.DetailView):
    model=Question
    template_name="polls/result.html"
    pk_url_kwarg='question_id'

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/result.html",{"question": question})
