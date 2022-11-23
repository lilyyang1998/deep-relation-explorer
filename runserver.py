# Adapted From:
# @inproceedings{TUD-CS-2017-0119,
# 	title = {{Context-Aware Representations for Knowledge Base Relation Extraction}},
# 	author = {Sorokin, Daniil and Gurevych, Iryna},
# 	booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
# 	pages = {1784-1789},
# 	year = {2017},
# 	location = {Copenhagen, Denmark},
# 	publisher = {Association for Computational Linguistics},
# 	doi = {10.18653/v1/D17-1188}
# }

import sys

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from relation_extraction.relextserver.server import relext

app.register_blueprint(relext, url_prefix="/relation-extraction")
app.run()