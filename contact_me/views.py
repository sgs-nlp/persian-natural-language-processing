from django.shortcuts import render
from django.http import HttpRequest


def contact_me_page_view(request: HttpRequest):
    return render(
        request,
        'contact_me/contact_me.html',
        context={},
    )