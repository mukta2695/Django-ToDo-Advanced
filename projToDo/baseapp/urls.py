from django.urls import path
from . views import TaskListView, DetailInfo, CreateTask, UpdateTask, DeleteTask, UserLogin, SignupPage, Home
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',TaskListView.as_view(), name='tasks'),#Depending on the post or get request, it will trigger that method in TaskListView class
    #path('task/<int:pk>/', DetailInfo.as_view(), name='task'), #Similarly, trigger method in detail info
    path('create-task/',CreateTask.as_view(), name='create-task'),
    path('update-task/<int:pk>/',UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/',DeleteTask.as_view(), name='delete-task'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('nearby-shops/', Home.as_view(), name='nearby-shops')
]