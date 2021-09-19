from hashlib import sha224


def string_hash(string: str):
    return sha224(string.encode('utf-8')).hexdigest()


def list_hash(value: list):
    string = str(value)
    return sha224(string.encode('utf-8')).hexdigest()
