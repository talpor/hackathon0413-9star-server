# Create your views here.
from NineStarServer.helpers.http import JsonResponse


def access_action(request, gate):
    """Try run the action script for the given gate"""
    if gate == '1':
        return JsonResponse({'success': True})
    elif gate == '2':
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
