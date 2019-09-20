def image_upload_location(dirname):
    return f'%Y-%m-%d/{dirname}/'

def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_agent(request):
    if 'User-Agent' in request.headers:
        user_agent = request.headers['User-Agent']
    else:
        user_agent = None
    return user_agent