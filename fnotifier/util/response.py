def response_json_ok(json):
    return _make_json_response(json, 200)


def response_json_bad_request(json):
    return _make_json_response(json, 400)


def response_json_unauthorized(json):
    return _make_json_response(json, 401)


def _make_json_response(json, status):
    return json, status, {'Content-Type': 'application/json'}