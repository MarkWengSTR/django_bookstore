from rest_framework.response import Response
from functools import wraps


def req_keys_check(keys=[]):
    def keys_check_deco(func):
        @wraps(func)
        def wrapper_func(request, *args, **kwargs):
            req_keys_ignore_format  = request.query_params.keys()-['format']
            if sorted(keys) == sorted(req_keys_ignore_format):
                return func(request, *args, **kwargs)
            else:
                return Response({"error_msg": "key error"})
        return wrapper_func
    return keys_check_deco


def req_params_in_key_check(params={}):
    """
    {'key': ['params1', 'params2']}
    """
    def params_check_deco(func):
        @wraps(func)
        def wrapper_func(request, *args, **kwargs):
            check_result = {
                "check": True,
                "error_msg": "",
            }
            for k, v_list in params.items():
                if request.query_params[k] not in v_list:
                    check_result["check"] = False
                    check_result["error_msg"] = "{0} params must in {1}".format(
                        k, v_list)

            if check_result["check"]:
                return func(request, *args, **kwargs)
            else:
                return Response({"error_msg": check_result["error_msg"]})
        return wrapper_func
    return params_check_deco
