from functools import wraps
from flask import render_template, session

def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'role' not in session:
                # Render a "Login" HTML page
                return render_template('login.html'), 403
            if session['role'] not in roles:
                # Render a "Login" HTML page
                return render_template('login.html'), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

