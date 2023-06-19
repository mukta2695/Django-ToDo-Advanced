from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import \
    LoginRequiredMixin  # Restricting unauthorized users
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import \
    reverse_lazy  # Used for redirecting the user to different page
from django.views.generic.detail import \
    DetailView  # Getting detailed information about a task
from django.views.generic.edit import \
    CreateView  # Import for creating the task/item
from django.views.generic.edit import DeleteView, FormView, UpdateView
#from django.http import HttpResponse
from django.views.generic.list import \
    ListView  # Getting the list view of all the tasks
#For Shop List
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

from .models import Task

# Create your views here.

'''def taskList(request):
    return HttpResponse('To-Do List')'''

#class for list view
class TaskListView(LoginRequiredMixin, ListView):
    model=Task
    context_object_name="list"

    #Inorder to seperate user specific data 
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['list']=context['list'].filter(user=self.request.user)
        context['count']=context['list'].filter(complete=False).count()

        #Search functionality
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['list']=context['list'].filter(title__startswith=search_input)
        context['search_input']=search_input
        return context

#class for detail information
class DetailInfo(LoginRequiredMixin,DetailView):
    model= Task
    context_object_name="task"

#class for creating an item
class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    #This will create a form automatically based on our model attribute
    #Listing out all the attributes. (We can selectively displaye the attributes by passing a python list of attributes)
    fields=['title','description', 'complete']   
    #When we create and submit an item/ task, send the user back on the list page
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CreateTask, self).form_valid(form)

#To update the task
class UpdateTask(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']  
    success_url=reverse_lazy('tasks')

#To delete the task
class DeleteTask(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="task"
    #Once we delete an item, redirect to main page
    success_url=reverse_lazy('tasks')

#For Login view
class UserLogin(LoginView):
    template_name='baseapp/login.html'
    fields='__all__'
    redirect_authenticated_user=True 

    def get_success_url(self):
        return reverse_lazy('tasks')

#For signing up new user
class SignupPage(FormView):
    template_name="baseapp/signup.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')

    
    def form_valid(self, form) :
        user=form.save()
        if user != None:
            login(self.request, user)
        return super(SignupPage,self).form_valid(form)

    def get(self, *args, **kwargs) :
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(SignupPage,self).get(*args, **kwargs)

longitude = -75.9334049178257
latitude =  42.104083499763114

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:5]
    template_name = 'shops/index.html'