from os import path
from json import loads, dumps

from flask import Response, request

# Load the JSON file with the data.
file_json = file(path.abspath('./app/data/math_phrases.json'))
data_json = file_json.read()
data_dict = loads(data_json)
file_json.close()


def phrases():
    if request.method == 'GET':
        lang = request.args.get('lang')

        if bool(lang):
            data = data_dict[lang]

            return Response(dumps(data), 200, {'Content-Type': 'application/json'})

    return Response(data_json, 200, {'Content-Type': 'application/json'})
