# Create your views here.
from NineStarServer.helpers.http import JsonResponse

from utils import gpio


def access_action(request, gate):
    """Try run the action script for the given gate"""
    if gate != '1' and gate != '2':
        return
    return JsonResponse({'success': gpio.open_gate(gate)})
