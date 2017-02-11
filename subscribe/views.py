# coding=utf-8
from django.core.mail import EmailMessage
from django.http import JsonResponse

from subscribe.models import Subscribe


def post(request):
    name = request.GET.get('name')
    phone_number = request.GET.get('phone')
    subscribe = Subscribe.objects.create(name=name, phone_number=phone_number)
    subscribe.save()
    e = EmailMessage('Подписка', ('Имя: '+str(name) + ", Тел: " + str(phone_number)),
                     from_email='tanaki.93@gmail.com', to=['testandsucces.93@gmail.com'])
    e.send()
    return JsonResponse(dict(result='thanks'))
