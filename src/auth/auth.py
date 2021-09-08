import json
from functools import wraps
from urllib.request import urlopen

from flask import request
from jose import jwt

DOMAIN = "lwinagency.us.auth0.com"
ALGORITHMS = ["RS256"]
API_IDENTIFIER= "http://localhost:9100"
CLIENT_ID = "wEWcJ1V4d64qCougsy9sZ7E02nkXhdDT"
CALLBACK_URL = "http://localhost:9100/main"

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


#get the jwt token from header
def get_token_auth_header():

    #check the Authorization include in request header
    if "Authorization" not in request.headers:
        raise AuthError(
            {"code": "not_found", "description": "Bearer Token Not Found"}, 401
        )

    #get the Authorization string
    authString = request.headers["Authorization"]

    #split the the Authorization string by space
    parts = authString.split(" ")

    #check Authorization header is correct format or not
    if parts[0] != "Bearer" or len(parts) != 2:
        raise AuthError(
            {"code": "invalid_token", "description": "Invalid Bearer Token"},
            401,
        )

    
    jwtToken = parts[1]

    #validate the jwt token format
    components = jwtToken.split(".")
    if len(components) != 3:
        raise AuthError(
            {"code": "invalid_token", "description": "Invalid Bearer Token"},
            401,
        )

    return jwtToken

#This is gonna be python decorator method for checking the permission
def check_permissions(permission, payload):

    #check the payload string whether permission keyword is include or not
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_token",
                "description": "Token format is invalid",
            },
            400,
        )
    
    if permission not in payload["permissions"]:
        raise AuthError(
        {"code": "unauthorized", "description": "Permission not granted"},
        403,
    )

    return True 

#this method to decode the jwt and return payload
def verify_decode_jwt(token):
    
    #get the public key
    jsonurl = urlopen(
        "https://{}/.well-known/jwks.json".format(DOMAIN)
    )
    
    #get the public key structure
    publickey_list = json.loads(jsonurl.read())

    rsa_key = {}

    for key in publickey_list["keys"]:        
        #get the kid value from public key
        if key["kid"] == jwt.get_unverified_header(token)["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
            break
    
    if rsa_key:
        try:                    
            #decode the jwt and return the payload
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_IDENTIFIER,
                issuer="https://{}/".format(DOMAIN),
            )            

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )

        except jwt.JWTClaimsError as error:
            print(str(error))
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token",
                },
                400,
            )
    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )

def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)

            return f(*args, **kwargs)

        return wrapper

    return requires_auth_decorator
