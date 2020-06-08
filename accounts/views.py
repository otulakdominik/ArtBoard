from django.shortcuts import (render, redirect, HttpResponse,
                              get_object_or_404, reverse, get_list_or_404, Http404)
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string


from .forms import SignUpForm, PostForm
from .tokens import account_activation_token
from .models import Post


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.account.birth_date = form.cleaned_data.get('birth_date')
            user.account. avatar = form.cleaned_data.get('avatar')
            user.account.facebook_url = form.cleaned_data.get('facebook_url')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate Your ArdBoard Account"
            message = render_to_string('accounts/email/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('accounts:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'accounts/email/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print('sadasdas')
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.account.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'accounts/email/account_activation_invalid.html')


def profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.user.username != user.username:
        user_posts = Post.objects.filter(author=request.user).order_by('created')

    else:
        user_posts = Post.objects.filter(author=request.user).order_by('created')

    #posts = paginate_result(request, user_posts, 15)

    return render(request, 'accounts/profile.html',
                   {'user': user, 'posts': user_posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/post_create.html', context)
