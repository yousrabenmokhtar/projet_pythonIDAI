from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from directChat.models import Message
from django.contrib.auth.models import User
from myApp.models import Utilisateur
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    utilisateur = get_object_or_404(Utilisateur, user=user)

    
    if messages:
        message = messages[0]
        active_direct = message['user'].username

        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'directs':directs,
        'utilisateur': utilisateur,
        'messages': messages,
        'active_direct': active_direct,
    }
    return render(request, 'pages/inbox.html', context)


@login_required
def Directs(request, username):
    user  = request.user
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    directs.update(is_read=True)

    for message in messages:
            if message['user'].username == username:
                message['unread'] = 0
    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }
    return render(request, 'pages/direct.html', context)


def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        redirect_url = reverse('directs', kwargs={'username': to_user_username})

        # Redirigez l'utilisateur vers la conversation avec le destinataire
        return redirect(redirect_url)
    else:
        # Gérer le cas où la méthode HTTP n'est pas POST
        pass


def UserSearch(request):
    query = request.GET.get('q')
    context = {}
    if query:
        # users = User.objects.filter(Q(username__icontains=query))
        users = Utilisateur.objects.filter(Q(Nom_complet__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)
        utilisateur = Utilisateur.objects.all()

        context = {
            'users': users_paginator,
            'query': query,  # Passer la requête de recherche au template
            "utilisateur"  :utilisateur,
            }

    return render(request, 'pages/search.html', context)

