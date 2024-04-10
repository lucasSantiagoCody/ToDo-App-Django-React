from django.core.exceptions import ValidationError



def validate_data_of_request(request_data):
   
    if not request_data['title']:
        raise ValidationError('title field must not be empty ')
    if not request_data['description']:
        raise ValidationError('description field must not be empty')
    if not request_data['status']:
        raise ValidationError('status field must not be empty')
    if not request_data['priority']:
        raise ValidationError('priority field must not be empty')
    
    return request_data