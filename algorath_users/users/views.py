from django.shortcuts import get_object_or_404, render

from .models import User, Connection


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


def find_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        user_name = request.POST['name']
        if not user_name:
            raise ValueError
    except ValueError:
        context = {'error_message': "You didn´t write the name.", 'user': user}
        return render(request, 'connections.html', context)
    else:
        user_list = User.objects.all().filter(user_name__icontains=user_name)
        context = {'user': user, 'user_list': user_list}
        return render(request, 'connections.html', context)


def connect_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        user_name = request.POST.get('connect_name', False)
        existing_user = User.objects.all().filter(user_name=user_name)[0]
        if not user_name:
            raise ValueError
        if Connection.objects.all().filter(from_user=user, to_user=existing_user):
            raise KeyError
    except ValueError:
        context = {'error_message': "You didn´t write the name.", 'user': user}
        return render(request, 'connections.html', context)
    except KeyError:
        context = {'error_message': user.user_name + " already has a connection with " + existing_user.user_name + ".",
                   'user': user}
        return render(request, 'connections.html', context)
    else:
        user.user_connections.add(existing_user)
        context = {'user': user}
        return render(request, 'connections.html', context)


