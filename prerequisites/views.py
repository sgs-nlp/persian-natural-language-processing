from django.shortcuts import render
from django.http import HttpRequest

from .controller import add_corpus_controller


def index(request: HttpRequest):
    pass


def add_corpus(request: HttpRequest):
    c_path = '/home/ya_hasan_mojtaba/my_projects/source_codes/django/persian_language_processing/static/HamshahriDataSample.xlsx'
    s_path = '/home/ya_hasan_mojtaba/my_projects/source_codes/django/persian_language_processing/static/HamshahriStopwordsList.xlsx'
    corpus_id = add_corpus_controller(c_path, s_path)
    print(corpus_id)
    pass
