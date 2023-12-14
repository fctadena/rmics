

def current_user_detail(request):
    return{'logged_in_user' : request.user}