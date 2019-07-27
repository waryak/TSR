from django.urls import path
from django.contrib import admin
from . import views

app_name = 'experiment'

urlpatterns = [path('', views.renderrr),
               path('admin', admin.site.urls)]


# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('test', views.renderrr, name='test')
# ]


# from django.urls import path
#
# from . import views
#
# app_name = 'polls'
#
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('test', views.renderrr, name='test')
# ]