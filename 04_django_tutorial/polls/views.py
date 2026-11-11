from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question,Choice


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




def detail(request,question_id):
    try: 
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questions not Found")
    # question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detial.html",{"question": question})



def vote(request,question_id):
    return HttpResponse("quesiton votes")