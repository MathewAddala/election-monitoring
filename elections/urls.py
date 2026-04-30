from django.urls import path
from . import views

app_name = 'elections'

urlpatterns = [
    path('',                    views.election_list,   name='list'),
    path('<int:pk>/',           views.election_detail, name='detail'),
    path('create/',             views.election_create, name='create'),
    path('<int:pk>/update/',    views.election_update, name='update'),
]