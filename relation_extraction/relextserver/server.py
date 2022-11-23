from flask import Blueprint, request, url_for, redirect
import json
import logging

from model import function

relext = Blueprint("relext_server", __name__, static_folder='static')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)
logger.setLevel(logging.DEBUG)


@relext.route("/")
def hello():
    return redirect(url_for('relext_server.static', filename='index.html'))


@relext.route("/parse/", methods=['GET', 'POST'])
def parse_sentence():
    if request.method == 'POST':
        input_text = request.json.get("inputtext")
        logger.debug("Processing the request")
        log = {}
        logger.debug("Prase")
        log['relation_graph'] = {
            'edgeSet': construct_relations_graph(input_text)
        }
        return json.dumps(log)
    return "No answer"


def construct_relations_graph(input_text):
    """
    The method seperates a string and produces a list of relations.

    :param input_text: a string with several names seperated by comma
    :return: list of dictionaries where each elements represent by the following order: source, target, correlation, and lexical tokens

    Tests:
    >>> construct_relations_graph("周杰倫,蔡依林,五月天")

    Return:
    >>> [{'left': '周杰倫', 'right': '蔡依林', 'kbID': '0.85', 'lexicalInput': 'couples'},
         {'left': '周杰倫', 'right': '五月天', 'kbID': '0.2', 'lexicalInput': 'friends'},
         {'left': '蔡依林', 'right': '五月天', 'kbID': '0.5', 'lexicalInput': 'enemies'}]
    """
    logger.debug("Seperating: {}".format(input_text))
    entities = input_text.split(",")
    logger.debug("Seperated: {}".format(input_text))
    logger.debug("Extract entities")
    parsed_graph = model.funtion(entities)
    return parsed_graph