import datetime

def track_access(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now()
        print(f"[{timestamp}] Accessing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def permission_check(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if getattr(user, "role", None) != required_role:
                raise PermissionError("Access denied")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
