import jwt
from functools import wraps
from django.http.response import HttpResponse,JsonResponse

def jwtencode(us):
    s="secured"
    encoded_jwt = jwt.encode(us, s, algorithm="HS256")
    print(encoded_jwt,"*******")
    return encoded_jwt
    

def jwtdecode(ss):
    s="secured"
    try:
        decode_jwt=jwt.decode(ss, s, algorithms=["HS256"])
        print(decode_jwt)
        return decode_jwt
    except:
        return "401"



def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        
        token = request.headers.get('Authorization', None)
        if not token or not token.startswith('Bearer '):
            return JsonResponse({"status": "UNAUTHORIZED"}, status=401)

        token_value = token.split('Bearer ')
        decoded_token = jwtdecode(token_value[1])

        if decoded_token == '401':
            return JsonResponse({"status": "UNAUTHORIZED..."}, status=401)

        request.decoded_token = decoded_token
        
        return view_func(request, *args, **kwargs)

    return _wrapped_view