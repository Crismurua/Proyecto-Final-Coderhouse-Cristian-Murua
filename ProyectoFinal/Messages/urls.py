from django.urls import path, re_path
from .views import *

app_name = 'Messages'

UUID_CHAT_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

urlpatterns = [
    re_path(UUID_CHAT_REGEX, ChatDetailView.as_view()),
	path("dm/<str:username>", private_messages, name='privatems'),
	path("ms/<str:username>", DetailMs.as_view(), name="detailms"),
	path("inbox/", Inbox.as_view(), name="inbox"),
]