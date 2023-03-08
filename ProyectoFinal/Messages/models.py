from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.
class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class ChatMessage(ModelBase):
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    
class ChatUser(ModelBase):
    chat = models.ForeignKey("Chat", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class ChatQuerySet(models.QuerySet):

	def only_one(self):
		return self.annotate(num_users=Count("users")).filter(num_users=1)

	def only_two(self):
		return self.annotate(num_users= Count("users")).filter(num_users=2)

	def filter_username(self, username):
		return self.filter(chatuser__user__username=username)

class ChatManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return ChatQuerySet(self.model, using=self._db)
    
    def filter_ms_private(self, username_a, username_b):
        return self.get_queryset().only_two().filter_username(username_a).filter_username(username_b)
    
    def get_ot_create_chat_current_user(self, user):
        qs = self.get_queryset().only_one().filter_username(user.username)
        if qs.exists():
            return qs.order_by("date").first, False
        
        chat_obj = Chat.objects.create()
        ChatUser.objects.create(user=user, chat=chat_obj)
        return chat_obj, True
	        

    def get_or_create_chat_ms(self, username_a, username_b):
        qs = self.filter_ms_private(username_a, username_b)
        if qs.exists():
            return qs.order_by("date").first(), False
        
        
        user_a, user_b = None, None
        try:
            user_a = User.objects.get(username=username_a)
        except User.DoesNotExist:
            return None, False
        
        try:
            user_b = User.objects.get(username=username_b)
        except User.DoesNotExist:
            return None, False
        
        if user_a == None or user_b ==None:
            return None, False
        
        obj_chat = Chat.objects.create()
        chat_user_a = ChatUser(user=user_a, chat=obj_chat)
        chat_user_b = ChatUser(user=user_b, chat=obj_chat)
        ChatUser.objects.bulk_create([chat_user_a, chat_user_b])
        return obj_chat, True
    
class Chat(ModelBase):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, through=ChatUser)
    objects = ChatManager()