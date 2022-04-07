from django.http import JsonResponse
from .dao_sample.user_dao_sample import get_all_users


def get_all_users_controller(request):
    data = get_all_users()[0]
    oid = str(data['_id'])
    return JsonResponse(oid, safe=False, status=200)
