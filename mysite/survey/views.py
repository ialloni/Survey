from multiprocessing.connection import answer_challenge
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from survey.forms import SurveyForm
from survey.models import Survey, PostQuestion, PostAnswer


# Create your views here.

def home(request):
    survey = Survey.objects.all()
    paginator = Paginator(survey, 3)
    page = request.GET.get('page')
    try:
        survey = paginator.page(page)
    except PageNotAnInteger:
        survey = paginator.page(1)

    return render(request, 'survey/home.html', {'survey': survey})


def list_survey(request, survey):
    survey = get_object_or_404(Survey, slug=survey)
    questions = survey.questions.all()
    for question in questions:
        answers = question.answers.all()


    return render(request, 'survey/list_survey.html', {'survey': survey,
                                                                        'questions': questions,
                                                                        })