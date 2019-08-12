from django.http import HttpResponse

from .models import User


def index(request):
    latest_user_list = User.objects.order_by('user_id')
    welcome = '<h2> Welcome to our Users app! </h2> ' \
              '<h4>These are some of the latest users added to the app: </h4>'
    output = ', <br>'.join([u.user_name for u in latest_user_list])
    return HttpResponse(welcome + output)

