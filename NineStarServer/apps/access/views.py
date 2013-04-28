# Create your views here.
from NineStarServer.helpers.http import JsonResponse

from utils import gpio


def access_action(request, gate):
    """Try run the action script for the given gate"""
    sleep = 1
    success = False
    if gate == '1' or gate == '2':
        if gate == '1':
            sleep = 5

        gpio.puss_button(gate, sleep)
        success = True

    return JsonResponse({'success': success})
