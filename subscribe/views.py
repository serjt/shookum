from django.http import JsonResponse

from subscribe.models import Subscribe


def post(request):
    name = request.GET.get('name')
    phone_number = request.GET.get('phone')
    subscribe = Subscribe.objects.create(name=name, phone_number=phone_number)
    subscribe.save()
    return JsonResponse(dict(result='thanks'))
