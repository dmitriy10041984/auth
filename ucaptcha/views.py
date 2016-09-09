from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import CaptchaForm

def home(request):
    if request.POST:
        form = CaptchaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = CaptchaForm()

    return render_to_response('captcha/home.html', dict(
        form=form), context_instance=RequestContext(request))





