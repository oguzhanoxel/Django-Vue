from django.http import JsonResponse

from .models import Coupon


def api_can_use(request):
    jsonresponse = {}

    coupon_code = request.GET.get('coupon_code', '')

    try:
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            jsonresponse = {'amount': coupon.value}
        else:
            jsonresponse = {'amount': 0}
    except Exception:
        jsonresponse = {'amount': 0}

    return JsonResponse(jsonresponse)
