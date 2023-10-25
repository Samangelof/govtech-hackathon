from .models import *

menu_reg_auth = [{'title':'Войти', 'url_name':'auth'},
                 {'title':'Создать аккаунт', 'url_name':'registration'},]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu_reg_auth

        return context