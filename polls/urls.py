from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # eg.: /polls/num/
    path('<int:question_id>/', views.detail, name='detail'),
    # eg. /polls/num/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # eg. /polls/num/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]