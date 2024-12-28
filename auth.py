from functools import wraps
from flask import render_template, session


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Render a "Login" HTML page
            return render_template('login.html'), 403
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'role' in session:
            if session['role'] != 'Admin':
                return render_template('login.html'), 403
        else:
            return render_template('login.html'), 403
        return func(*args, **kwargs)
    return wrapper

