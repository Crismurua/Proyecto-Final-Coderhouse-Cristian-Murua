from django.contrib import admin
from .models import Chat, ChatUser, ChatMessage

# Register your models here.
class ChatMessageInline(admin.TabularInline):
	model = ChatMessage
	extra = 1

class ChatUserInline(admin.TabularInline):
	model = ChatUser
	extra = 1


class ChatAdmin(admin.ModelAdmin):
	inlines = [ChatMessageInline, ChatUserInline]

	class Meta:
		model = Chat

admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatUser)
admin.site.register(ChatMessage)
