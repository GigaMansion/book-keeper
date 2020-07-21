from functools import wraps
from flask import request, jsonify

import jwt

from book_keeping_backend_package import token_redis_db

def generate_token(secret):

    encoded_jwt = jwt.encode({"string": "liang shen zui shuai!"}, secret, algorithm='HS256')

    return encoded_jwt


def revoke_token():
    pass


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = None
        
        if 'authorization' in request.headers:
         token = request.headers['authorization']

        if not token:
            return jsonify({'message': 'missing token'})

        try:
            user_email = token_redis_db.get(token)
            print("token found!", token)
        except:
            return jsonify({'message': 'token invalid'})

        return f(user_email, *args, **kwargs)

    return decorated_function