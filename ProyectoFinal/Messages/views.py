from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import ChatMessage, ChatUser, Chat
from django.http import HttpResponse, Http404, JsonResponse
from .forms import MessageForm
from django.views.generic.edit import FormMixin
from django.views.generic import View


# Create your views here.
class Inbox(View):
	def get(self, request):

		inbox = Chat.objects.filter(chatuser__user__in=[request.user.id])
		context = {
			"inbox":inbox
		}
		return render(request, 'inbox.html', context)

class ChatFormMixin(FormMixin):
	form_class = MessageForm
	#success_url = "./"

	def get_success_url(self):
		return self.request.path

	def post(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			raise PermissionDenied

		form = self.get_form()
		if form.is_valid():
			chat = self.get_object()
			user = self.request.user 
			message = form.cleaned_data.get("message")
			chat_obj = ChatMessage.objects.create(chat=chat, user=user, text=message)
			
			if request.is_ajax():
				return JsonResponse({

					'message':chat_obj.text,
					'username':chat_obj.user.username
					}, status=201)

			return super().form_valid(form)

		else:

			if request.is_ajax():
				return JsonResponse({"Error":form.errors}, status=400)

			return super().form_invalid(form)

class ChatDetailView(LoginRequiredMixin, ChatFormMixin, DetailView):
	template_name= 'chat-detail.html'
	queryset = Chat.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		obj = context['object']
		print(obj)

		#if self.request.user not in obj.usuarios.all():
		#	raise PermissionDenied

		context['member_chat'] = self.request.user in obj.users.all()

		return context

class DetailMs(LoginRequiredMixin, ChatFormMixin, DetailView):

	template_name= 'chat-detail.html'

	def get_object(self, *args, **kwargs):

		username = self.kwargs.get("username")
		my_username = self.request.user.username
		chat, _ = Chat.objects.get_or_create_chat_ms(my_username, username)

		if username == my_username:
			my_chat, _ = Chat.objects.get_ot_create_chat_current_user(self.request.user)

			return my_chat

		if chat == None:
			raise Http404

		return chat

def private_messages(request, username, *args, **kwargs):

	if not request.user.is_authenticated:
		return HttpResponse("Not Allowed")

	my_username = request.user.username

	chat, created = Chat.objects.get_or_create_chat_ms(my_username, username)

	if created:
		print("Created")

	Users_Chat = chat.chatuser_set.all().values("user__username")
	print(Users_Chat)
	chat_message  = chat.chatmessage_set.all()
	print(chat_message.values("text"))

	return HttpResponse(f"Chat ID - {chat.id}")
