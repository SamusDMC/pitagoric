import mimetypes

from flask import Response

mimetypes.add_type('.json', 'application/json')


def content_type(ext):
    """
    Function for get content-type header.
    """

    ext = '.' + ext

    return {
        'Content-Type': mimetypes.types_map[ext]
    }


def access_denied_res(error):
    """
    Response for access denied (UNAUTHORIZED - 401).
    """

    headers = {
        'WWW-Authenticate': 'Basic realm="Login Required"',
        'Content-Type': mimetypes.types_map['.json'],
    }

    return Response(error, 401, headers)


def not_found_res():
    """
    Response for not found (404).
    """

    return Response('Not found', 404)
