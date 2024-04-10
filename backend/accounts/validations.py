from .models import CustomUser
from django.core.exceptions import ValidationError


# esta funcão retorna  um dicionario com duas chaves 
# a primeira é retorna os mesmos dados passados pela requisição
# a segunda retorna uma lista de possíveis erros de validação

def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    errors = []

    if not email or CustomUser.objects.filter(email=email).exists():
        errors.append('use another email')
    if not username:
        errors.append('username must not be empty')
    if not password or len(password) < 8:
        errors.append('password must not be empty and min 8 characters')
    
    custom_data = {
        'data': data,
        'errors': errors
    }
    return custom_data

