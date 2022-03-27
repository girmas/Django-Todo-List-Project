from django.urls import path
from .import views
urlpatterns = [
    
     path('',views.home,name='home'),
     path('register',views.register_user,name='register'),
     path('login',views.login_user,name='login'),
     path('todo',views.todotask,name='todo'),
     path('logout',views.logout_user,name='logout'),
     path('delete_task/<str:pk>',views.delete_task,name='deletetask'),
     path('update_task/<str:pk>',views.update_task,name='updatetask'),
     path('change_password',views.change_password,name='changepass')
     
     
     
 ]


