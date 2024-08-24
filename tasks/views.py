from django.shortcuts import render, redirect
from .models import *
# Create your views here.



def task_list(request):
    tasks = Task.objects.all()

    print(tasks)
    return render(request, 'task_list.html', {'tasks': tasks})

def task_details(request,t_id):
    task = Task.objects.get(t_id=t_id)
    return render(request, 'task_details.html', {'task': task})



def task_create(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            status = request.POST.get('status')
            priority = request.POST.get('priority')
            due_date = request.POST.get('due_date')
            # category = request.POST.get('category')
            category = TaskCategoy.objects.get(name=request.POST.get('category'))
            # assigned_to = request.POST.get('assigned_to')
            assigned_to = Member.objects.get(name=request.POST.get('assigned_to'))

            print("TASK CATEGORY,---",category)

            task = Task.objects.create(title=title,description=description,status=status,priority=priority,due_date=due_date,category=category,assigned_to=assigned_to)
            task.save()
            return redirect('task_list')
        except Exception as e:
            print(e)
    member = Member.objects.all()
    task_category = TaskCategoy.objects.all()
    print("MEMBER---",member)
    return render(request, 'task_create.html',{'member':member,'task_category':task_category})



def task_update(request,t_id):
    try:
        task = Task.objects.get(t_id=t_id)
        members = Member.objects.all()
        category = TaskCategoy.objects.all()
        print("TASK",task.t_id)
        if request.method == 'POST':

            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.priority = request.POST.get('priority')
            task.due_date = request.POST.get('due_date')
            task.category = TaskCategoy.objects.get(name=request.POST.get('category'))
            task.assigned_to = Member.objects.get(name=request.POST.get('assigned_to'))
            
            task.save()

            print("SUCESSS________________")
            return redirect('task_list')
        return render(request, 'task_update.html',{'task':task,'member':members,'category':category})
    except Exception as e:
        print('EXCEPTTION+=============',e)

def task_delete(request,t_id):
    task = Task.objects.get(t_id=t_id)
    task.delete()
    return redirect('task_list')


def users_create(request):
    try:
        if request.method == 'POST':
            print("USER")
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(first_name=name,username=email,password=password)
            
            Member.objects.create(name=name, email=email,password=password,)
            
                            
            print("USER CREATED")

            return redirect('user_list')
        return render(request, 'user_create.html')
    
    except Exception as e:
        print('EXCEPTTION+=============',e)


def user_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html',{'members':members})



def category_create(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            
            category = TaskCategoy.objects.create(name=name,description=description)
            print("CATEGORY CREATED")
            return redirect('categories')
        return render(request, 'category_create.html')
    except Exception as e:
        print('EXCEPTTION+=============',e)

def categories(request):
    categories = TaskCategoy.objects.all()
    return render(request, 'category_list.html',{'categories':categories})