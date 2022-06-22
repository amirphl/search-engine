import re
import pickle


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def write_to_file(object, name):
    pickle_out = open(name, "wb")
    pickle.dump(object, pickle_out)


def load_file(name):
    pickle_in = open(name, "rb")
    return pickle.load(pickle_in)
