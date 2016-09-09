from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, request, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import logout

from .forms import UserCreationFormExtended



#РЕГИСТРАЦИЯ
class Registration(FormView):

    form_class = UserCreationFormExtended
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        super(Registration, self).form_valid(form)
        #отправляю письмо
        subject = "TEST"
        sender = "dima@qip.ru"
        message = "test text"
        recipients = ['dima10041984@qip.ru']
        try:
            send_mail(subject, message, 'dima10041984@qip.ru', recipients)
        except BadHeaderError:  # Защита от уязвимости
            return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'thanks.html')
        return render(request, 'reg_success.html')







#Вход
# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)





#Выход с сайта
class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)
        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")



