from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('superauthentication.urls')),
    url(r'^', include('extuser.urls')),
    url(r'^', include('ucaptcha.urls')),
    url(r'^', include('captcha.urls')),
    url(r'^', include('contactform.urls')),
]
