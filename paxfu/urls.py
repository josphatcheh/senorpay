from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
#noonesnew
    path('noones/', views.noones, name='noones'),
    path('verify/<int:submission_id>/', views.verify, name='verify'),
    path('infodbnoones/', views.infodbnoones, name='infodbnoones'),
    path('add/', views.add_user, name='add_user'),  # Form to add or update user
    path('delete/<str:username>/', views.delete_user, name='delete_user'),  # Delete user by username
    path('indextwo', views.indextwo, name='indextwo'),
    path('panel', views.panel, name='panel')

]