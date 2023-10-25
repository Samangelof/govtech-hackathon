from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm
from schools.forms import RegisterStudentForm, AuthUserForm
from schools.models import Schools, Students
from django.views.generic import FormView, View
from django.contrib.auth import authenticate



menu = [{'title': 'Главная', 'url_name':'home'},
        {'title': 'О сайте', 'url_name':'about'},
        {'title': 'Добавить статью', 'url_name': 'add_article'},
        {'title': 'Войти', 'url_name': 'auth'}]

menu_schools_region =  [{'title': 'Новый город', 'url_name':'noviy-gorod'},
                        {'title': 'Юго-восток', 'url_name':'ugo-vostok'},
                        {'title': 'Пришахтинск', 'url_name':'prishahtinsk'},
                        {'title': 'Сортировка', 'url_name':'sortirovka'},
                        {'title': 'Майкудук', 'url_name':'maikuduk'}]

menu_reg_auth = [{'title':'Войти', 'url_name':'authorization'},
                 {'title':'Создать аккаунт', 'url_name':'registration'},]


def index(request):
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'menu_schools_region': menu_schools_region,
    }
    return render(request, 'schools/hackaton.html', context=context)


class RegistrationStudent(CreateView):
    form_class = RegisterStudentForm
    template_name: str = 'schools/sing-in.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация учеников'
        return context

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('home')
    


class AuthorizationStudent(FormView):
    template_name = 'schools/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        user = authenticate(
            request=self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user:
            login(self.request, user)
            return redirect(reverse("home"))
        else:
            return render(
                request=self.request,
                template_name='schools/login.html',
                context={
                    'form': form,
                    'error': "Не верное имя пользователя или пароль"
                }
            )


def personal_kab(request):
    return render(
        request, 'schools/personal_kab.html',
    )


def administration(request):
    return render(
        request, 'schools/change.html',
    )


def schools(request):
    return render(
        request, 'schools/schools.html',
    )


class Search(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        all_products = Schools.objects.all()
        search_products = []
        for item in all_products:
            if request.POST.get('search').lower() in item.title.lower():
                search_products.append(item)
        return render(
            request=request,
            template_name="schools/search.html",
            context={"search": search_products}
        )


def view_schools(request):
    schools = Schools.objects.all()
    context = {'schools': schools}
    return render(
        request, context=context,
        template_name='schools/schools.html'
    )



# class AuthorizationStudent(LoginView):
#     form_class = AuthUserForm 
#     template_name: str = 'schools/login.html'

#     def get_context_data(self, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Авторизация учеников'
#         return context

#     def get_success_url(self):
#         return reverse_lazy('home')
    




def logout_user(request):
    logout(request)
    return redirect('register')




def thanks(request): return render(request, 'schools/thanks.html')



def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Not found 404</h1>')