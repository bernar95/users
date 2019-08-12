from django.shortcuts import get_object_or_404, render

from .models import User


def index(request):
    user_list = User.objects.order_by('user_id')
    context = {'user_list': user_list}
    return render(request, 'index.html', context)


def connections(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'connections.html', {'user': user})


def add_user(request):
    user_list = User.objects.order_by('user_id')
    try:
        user_name = request.POST['name']
        existing_user = User.objects.all().filter(user_name=user_name)
        if not user_name:
            raise ValueError
        if existing_user:
            raise KeyError

    except ValueError:
        context = {'error_message': "You didn´t write the name.", 'user_list': user_list}
        return render(request, 'index.html', context)
    except KeyError:
        context = {'error_message': "There is an existing user with that name.", 'user_list': user_list}
        return render(request, 'index.html', context)
    else:
        user = User(user_name=user_name)
        user.save()
        return render(request, 'index.html', {'user_list': user_list})

