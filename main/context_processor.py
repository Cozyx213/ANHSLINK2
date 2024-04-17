from authentication.models import Profile


def user_profile(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    return {'user': profile}