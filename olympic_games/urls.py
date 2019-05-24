from django.urls import path, include

from . import views

app_name = 'olymipic_games'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('results/', views.ResultsDisciplinePageView, name='results_by_discipline')
]