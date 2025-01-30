from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from django.views.decorators.http import require_POST
from survey.forms import CommentForm
from survey.models import Survey


# Create your views here.
@require_POST
def survey_comment(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    comment = None
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.survey = survey
        comment.save()

    return render(request, 'survey/comment.html', {'survey': survey,
                                                                        'form': form,
                                                                        'comment': comment,
                                                                        })

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
    questions = survey.questions.all().prefetch_related('answers')

    questions_with_answers = []
    for quest in questions:
        answers = quest.answers.all()
        questions_with_answers.append({
            'question': quest,
            'answers': answers
        })

    comments = survey.comments.filter(active=True)
    form = CommentForm()


    return render(request, 'survey/list_survey.html', {'survey': survey,
                                                                        'questions': questions,
                                                                        'comments': comments,
                                                                        'form': form,
                                                                        'questions_with_answers': questions_with_answers,
                                                                        })