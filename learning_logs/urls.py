"""Define URL patterns for leraning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page fo r a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
