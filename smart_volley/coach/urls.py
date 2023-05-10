from django.urls import path

from . import views
from .views import CoachListView, CoachCreateView


urlpatterns = [
    path('', CoachCreateView.as_view(), name='create_coach'),
    path('list/', CoachListView.as_view())
]

