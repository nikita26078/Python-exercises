from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import NewsForm, FeedbackForm, UserRegistrationForm, LoginForm
from .models import News, Category


def contact(request):
    return render(request, 'app/contact.html')


def about(request):
    return render(request, 'app/about.html')


def gallery(request):
    return render(request, 'app/gallery.html')


class NewsListView(ListView):
    model = News
    paginate_by = 12
    template_name = 'app/home.html'
    context_object_name = 'app'
    queryset = News.objects.order_by('-date')


class CategoryListView(ListView):
    model = Category
    template_name = 'app/categories.html'


class CategoryNewsListView(ListView):
    model = News
    template_name = 'app/home.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_name'])
        return News.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            error = 'Ошибка валидации'
    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'app/news_add.html', data)


def feedback(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            error = 'Ошибка валидации'
    form = FeedbackForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'app/feedback.html', data)


def profile(request):
    if request.user.is_anonymous:
        return user_login(request)
    else:
        ln = len(News.objects.filter(user=request.user.profile.user))
        data = {
            'profile': request.user.profile.user,
            'posts': ln
        }
        return render(request, 'app/profile.html', data)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'app/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'app/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'app/login_done.html', {'new_user': user})
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return HttpResponse('Неверные данные')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


def search(request):
    q = request.GET['query']
    mydictionary = {
        "object_list": News.objects.filter(title__contains=q)
    }
    return render(request, "app/home.html", context=mydictionary)
