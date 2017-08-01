from os import path
from json import loads, dumps

from flask import Response, request

from ..helpers.res_helpers import content_type, not_found_res

# Load the JSON file with the data.
file_json = file(path.abspath('./app/data/math_phrases.json'))
data_json = file_json.read()
data_dict = loads(data_json)
file_json.close()


def phrases():
    """
    Functional route for get fhrases of mathematics.
    """

    if request.method == 'GET':
        lang = request.args.get('lang')
        limit = request.args.get('limit')
        headers = content_type('json')

        if lang is not None:
            data = data_dict[lang][:int(limit) or len(data_dict[lang])]

            return Response(dumps(data), 200, headers)
        else:
            return not_found_res()

        return Response(data_json, 200, headers)
