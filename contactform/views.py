from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django import forms

#Форма для обратной связи
class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	message = forms.CharField()
	copy = forms.BooleanField(required = False)


def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']

			recipients = ['dima10041984@qip.ru']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'dima10041984@qip.ru', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'contact.html', {'form': form})