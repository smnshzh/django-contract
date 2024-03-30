def current_user(request):
    # Return a dictionary with the current user's username
    return {'current_user': request.user}