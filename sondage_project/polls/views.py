from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

# Create your views here.

### v4
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        ### v4
        # """Return the last five published questions.
        # """
        # return Question.objects.order_by('-pub_date')[:5]

        ### v5
        """ Return the last five published questions (
            not including those set to be published in the future).
        """
        return Question.objects.filter(
                pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

### v1
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
    ### v1
    # question = Question.objects.get(pk=question_id)
    # return HttpResponse("Your're looking at question %s." % question_id)


    ### v2
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {
    #             'question': question}
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'polls/detail.html', context)


    ### v3
    # question = get_object_or_404(Question, pk=question_id)
    # context = {
    #     'question': question}
    # return render(request, 'polls/detail.html', context)


# def results(request, question_id):
    ### v1
    # response = "You're looking at the result of question %s."
    # return HttpResponse (response % question_id)

    ### v2
    # question = get_object_or_404(Question, pk=question_id)
    # context = {
    #     'question': question
    # }
    # return render(request, 'polls/results.html', context)


def vote(request, question_id):
    ### v1
    # return HttpResponse("You're voting on question %s." % question_id)

    ### v2
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
