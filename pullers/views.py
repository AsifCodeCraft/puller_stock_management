from django.shortcuts import render, get_object_or_404
from .models import Puller, UserProfile
from .models import BodyParts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'pullers/page-login.html')


def logout_view(request):
    logout(request)
    return redirect('login')




def _filtered_puller_list(request, category=None):
    """Common logic — category filter সহ search"""
    pullers = Puller.objects.all().order_by('-created_at')

    if category:
        pullers = pullers.filter(category__category=category)

    code = request.GET.get('code', '').strip()
    name = request.GET.get('name', '').strip()
    size = request.GET.get('size', '').strip()

    if code:
        pullers = pullers.filter(puller_code__icontains=code)
    if name:
        pullers = pullers.filter(puller_name__icontains=name)
    if size:
        pullers = pullers.filter(puller_size__icontains=size)

    context = {
        'pullers': pullers,
        'code': code,
        'name': name,
        'size': size,
        'total_pullers': pullers.count(),
        'category': category,
    }

    return render(request, 'pullers/puller_list.html', context)

@login_required
def puller_list(request):
    # সব puller (কোনো category filter ছাড়া) — সরাসরি /puller_list এ গেলে
    return _filtered_puller_list(request, category=None)

@login_required
def special_puller_page(request):
    return _filtered_puller_list(request, category='special')


@login_required
def da_puller_page(request):
    return _filtered_puller_list(request, category='da')


@login_required
def dalh_puller_page(request):
    return _filtered_puller_list(request, category='dalh')


@login_required
def puller_detail(request, pk):
    puller = get_object_or_404(Puller, pk=pk)
    category = request.GET.get('category', '')

    context = {
        'puller': puller,
        'category': category,
    }
    return render(request, 'pullers/puller_detail.html', context)


@login_required
def home(request):
    return render(request, 'pullers/home.html')


@login_required
def puller_page_menu(request):
    # Special / Regular বাছাই করার page
    return render(request, 'pullers/puller_page.html')


@login_required
def regular_puller_menu(request):
    # DA / DALH বাছাই করার page
    return render(request, 'pullers/regular_puller_page.html')


@login_required
def dashboard(request):
    # DA / DALH বাছাই করার page
    return render(request, 'pullers/dashboard.html')