import os
import openpyxl

from nvd.hasher import string_hash
from nvd.pre_processing import tokenizer, normilizer

from .models import Corpus

from conf.settings import BASE_DICT


def _stopwords_list(file_path):
    wb_obj = openpyxl.load_workbook(file_path)
    sheet = wb_obj.active
    return [word2db(row[0].value) for row in list(sheet.iter_rows())[1:]]


def add_corpus_controller(corpus_file_path: str, stopwords_list_file_path: str):
    corpus = Corpus(file_path=corpus_file_path)
    corpus.save()
    return corpus.pk
