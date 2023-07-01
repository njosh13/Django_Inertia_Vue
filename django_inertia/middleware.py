from inertia import share
from django.conf import settings
from django.contrib.auth.models import AnonymousUser


def inertia_share(get_response):
  def middleware(request):
    share(request, 
      # app_name=settings.APP_NAME,
      # user_count=lambda: User.objects.count(), # evaluated lazily at render time
      user=lambda: request.user if not isinstance(request.user, AnonymousUser) else None, # evaluated lazily at render time
    )

    return get_response(request)
  return middleware