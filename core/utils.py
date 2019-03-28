from functools import wraps


def user_passes_test(test_func):
    def decorator(resolve_func):
        @wraps(resolve_func)
        def _wrapped_resolve(*args, **kwargs):
            user = args[1].context.user
            if test_func(user):
                return resolve_func(*args, **kwargs)
            raise Exception('Usuário não está logado')
        return _wrapped_resolve
    return decorator


def token_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
