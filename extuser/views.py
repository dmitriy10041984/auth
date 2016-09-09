from django.http.response import HttpResponse, Http404, HttpResponseRedirect
#отвечает за получение шаблона
from django.template.loader import get_template
#отвечает за хранение переменных, которые будут огтправлены потом в шаблон
from django.template import loader, Context, RequestContext
from django.shortcuts import render_to_response, redirect, render
from extuser.models import ExtUser
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth




