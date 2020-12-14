from django.urls import path
from .views import ParticipantView, NotificationView

urlpatterns = [
    path('post/participant/', ParticipantView.as_view()),
    path('post/notification/', NotificationView.as_view()),
]
