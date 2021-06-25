from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='login')
def index(request, *args, **kwargs):
    print(args, kwargs)
    print("INDEX TEMPLATE")
    print("USER LOGIN: ", request.user,)

    return render(request, 'pk_main_website/index.html')


def profile(request, *args, **kwarg):
    print("About TEMPLATE")
    print(request.user)

    context = {
        "user_name": request.user,
        "email": request.user.email,
    }

    return render(request, 'pk_main_website/profile.html', context)

@login_required
def board(request, *args, **kwargs):
    print(args, kwargs)
    print("BOARD TEMPLATE")

    boards = Board.objects.filter(owner=request.user)
    board_form = Board_Form()

    if request.method == 'POST':
        board_Form = Board_Form(request.POST)
        if board_form.is_valid():
            board_form.save()
        return redirect('board')
 
    context = {
        'user_name': request.user,
        'boards' : boards,
        'board_form': board_form
    }

    print("USER LOGIN: ", request.user)
    print("This is ",request.user, " board: ", boards)

    return render(request, 'pk_main_website/board.html', context)

def board_creation(request):

    print("BOARD creation TEMPLATE")
    print(request.user)

    board_form = Board_Form()

    if request.method == 'POST':
        board_form = Board_Form(request.POST)
        if board_form.is_valid():
            board_form.save()
        return redirect('board')

    context = {
        'board_form' : board_form
    }

    return render(request, 'pk_main_website/board_creation.html', context)


#create Board detail view for each board
def board_detail(request, pk):

    print("Baord Detail TEMPLATE")
    print("USER LOGIN: ", request.user)
    
    board = Board.objects.get(id = pk)
    board_form = Board_Form(instance=board)

    if request.method == 'POST':
        board_form = Board_Form(request.POST, instance=board)
        if board_form.is_valid():
            board_form.save()
        return redirect('board')

    context = {
        'board_form': board_form,
       
    }

    return render(request, 'pk_main_website/board_detail.html', context)

def delete_board(request, pk):
    print("Baord Delete TEMPLATE")
    print("USER LOGIN: ", request.user)

    board = Board.objects.get(id=pk)

    if request.method == 'POST':
        board.delete()
        return redirect('board')

    context = {
        
            'board' : board,
    }

    return render(request, 'pk_main_website/delete_board.html', context)


@login_required
def task_view(request, *args, **kwargs):
    print(args, kwargs)
    print("Task TEMPLATE")
    print("USER LOGIN: ", request.user)

    # tasks = Task.objects.all()
    # tasks = Task.objects.get(id=1)
    tasks = Task.objects.filter(owner=request.user)
    form = Task_Form()

    if request.method == 'POST':
        form = Task_Form(request.POST)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.owner = request.user
            # instance.save()

            form.save()
            
        return redirect('task')

    context = { 'tasks':tasks, 'form':form }

    return render(request, 'pk_main_website/task.html', context)


def update_task(request, pk):

    task = Task.objects.get(id = pk)

    form = Task_Form(instance=task)

    if request.method == 'POST':
        form = Task_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')

    context = {'form':form}
    
    return render(request, 'pk_main_website/update_task.html', context)


def delete_task(request, pk):

    item = Task.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('task')

    context = { 'item':item}

    return render(request, 'pk_main_website/delete_task.html', context)


def category_view(request):

    print("Task TEMPLATE")
    print("USER LOGIN: ", request.user)

    categories = Category.objects.filter(owner=request.user)
    category_form =Category_Form()

    context = {
        'categories' : categories,
    }

    return render(request, 'pk_main_website/category.html', context)


def category_creation(request):

    category_form = Category_Form()

    if request.method == 'POST':
        category_form = Category_Form(request.POST)
        if category_form.is_valid():
            category_form.save()
        return redirect('category')

    context = {
        'category_form' : category_form,
    }
    return render(request, 'pk_main_website/category_creation.html', context)


def category_detail(request, pk):

    category = Category.objects.get(id=pk)
    category_form = Category_Form(instance=category)

    if request.method == 'POST':
        category_form = Category_Form(request.POST,instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect('category')

    context = {
        'category':category,
        'category_form' : category_form,

    }

    return render(request, 'pk_main_website/category_detail.html', context)


def delete_category(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category')

    context = {
        'category' :category,
    }

    return render(request, 'pk_main_website/delete_category.html', context)



# define task in category view
def task(request, task_id):

    try:
        task = Task.objects.get(id=task_id)
    except Item.DoesNotExist:
        task=None
    
    context={
        'task' : task
    }

    return render(request, 'pk_main_website/category.html', context)