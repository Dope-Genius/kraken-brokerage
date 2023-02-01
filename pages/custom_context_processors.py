from django.contrib.auth.models import User
from pages.models import Notification
# from django.core.context_processors import request
# from django.core.context_processors import request

def subject_renderer(request):
  if request.user.is_authenticated:
    return {'notify_count': Notification.objects.filter(user=request.user)}
  return {}