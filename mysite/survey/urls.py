from django.urls import path

from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.home, name='home'),

    path('<slug:survey>/', views.list_survey, name='list_survey'),
]
