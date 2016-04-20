from django.shortcuts import render
from django.http import HttpResponse
from bp import get_bp
from models import Pages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def showPages(request):
    pageList = Pages.objects.all()
    answer = "<ol>"
    for page in pageList:
        answer += '<li><a href="/' + str(page.id) + '">' + page.name + '</a>'
    answer += "</ol>"
    return HttpResponse(answer)

def insert(request, arg1, arg2):
    newPage = Pages(name=arg1, page=arg2)
    newPage.save(),
    answer = "200 OK"
    return HttpResponse(answer)

def viewPage(request, identificator):
    try:
        answer = ""
        bp = get_bp()
        page = Pages.objects.get(id=identificator)
        answer += page.page + '</br>'
        answer += '<p>' + bp +'</p>'
    except ObjectDoesNotExist:
        answer = "The page does not exists."
    return HttpResponse(answer)
