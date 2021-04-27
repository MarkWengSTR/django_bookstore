from rest_framework.response import Response


def req_keys_check(keys=[]):
    def keys_check_deco(func):
        def wrapper_func(request, *args, **kwargs):
            if sorted(keys) == sorted(request.query_params.keys()):
                return func(request, *args, **kwargs)
            else:
                return Response({"error_msg": "key error"})
        return wrapper_func
    return keys_check_deco
