from django.shortcuts import render
from django.http import HttpRequest


def about_me_page_view(request: HttpRequest):
    return render(
        request,
        'about_me/about_me.html',
        context={},
    )