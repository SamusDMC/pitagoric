from flask import Response


def access_denied_res(error):
    """Response for access denied (UNAUTHORIZED - 401)"""

    headers = {
        'WWW-Authenticate': 'Basic realm="Login Required"',
        'Content-Type': 'application/json',
    }

    return Response(error, 401, headers)


def invalid_token_res(error):
    """Response for invalid tokens"""

    headers = {
        'Content-Type': 'application/json',
    }

    return Response(error, 401, headers)
