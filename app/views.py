import copy

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for question # {i}',
        'tags': ['blablabla'] if i % 2 == 0 else ['other_tag']
        # 'tag': f'tag #{i}'
    } for i in range(30)
]

ANSWERS = [
    {
        'id': i,
        'text': f'This is text for answer # {i}'
                f'Lorem ipsum dolor sit amet consectetur adipisicing elit.'

    } for i in range(20)
]


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')  

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page



def index(request):
    paginated_questions = paginate(QUESTIONS, request, per_page=5)

    return render(
        request,
        'index.html',
        context={
            'questions': paginated_questions.object_list,
            'page_obj': paginated_questions
        }
    )



def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    paginated_questions = paginate(hot_questions, request, per_page=5)

    return render(
        request,
        'hot.html',
        context={
            'questions': paginated_questions.object_list,
            'page_obj': paginated_questions
        }
    )



def question(request, question_id):

    one_question = QUESTIONS[question_id]

    paginated_questions = paginate(ANSWERS, request, per_page=5)

    return render(
        request,
        'question.html',
        context={
            'question': one_question,
            'answers': paginated_questions.object_list,
            'page_obj': paginated_questions
        }
    )




def login(request):
    return render(
        request, 'login.html',
        context={'questions': login}
    )


def singup(request):
    return render(
        request, 'singup.html',
        context={'questions': login}
    )


def setting(request):
    return render(
        request, 'setting.html',
        context={'questions': setting}
    )

def ask(request):
    return render(
        request, 'ask.html',
        context={'questions': ask}
    )


TAG = [
    {
        'title': f'Tag {i}'
    } for i in range(30)
]

def tag(request):

    paginated_questions = paginate(QUESTIONS, request, per_page=5)

    return render(
        request,
        'tag.html',
        context={
            'questions': paginated_questions.object_list,
            'page_obj': paginated_questions
        }
    )



def tag(request, tag_name):
    tagged_questions = [q for q in QUESTIONS if tag_name in q.get('tags', [])]
    


    paginated_questions = paginate(tagged_questions, request, per_page=5)

    
    return render(
        request,
        'tag.html',
        context={
            'tag': tag_name,
            'questions': paginated_questions.object_list,
            'page_obj': paginated_questions
        }
    )
