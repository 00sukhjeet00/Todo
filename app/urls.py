from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('addTodo', views.addTodo, name='addTodo'),
    path('signout', views.signout, name='signout'),
    path('delete/<str:title>', views.delete, name='delete'),
    path('change/<str:title>', views.change, name='change'),
    path('deleteAccount', views.deleteAccount)
]
