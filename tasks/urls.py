from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.task_list,name='task_list'),
    path('task_create/',views.task_create,name='task_create'),
    path('task_update/<int:t_id>/',views.task_update,name='task_update'),
    path('task_delete/<int:t_id>/',views.task_delete,name='task_delete'),
    path('users/',views.user_list,name='user_list'),
    path('user_create/',views.users_create,name='user_create'),
    path('category_create/',views.category_create,name='category_create'),
    path('categories/',views.categories,name='categories'),

]
