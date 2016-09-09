from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


from extuser import views

urlpatterns = [

]

#Если картинки не отображаются, на реальном сервере они отобразятся, необходимо указать
#если режим отладки, то должны использовать данную строку
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


