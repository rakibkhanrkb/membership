from django.shortcuts import render
from django.utils import timezone
from .models import reg, bitboxc, SupportMessage, VisitorCount, VisitorIP
from itertools import chain

def index(request):
    # bitbox data
    inf = bitboxc.objects.all()

    # visitor counter
    counter, created = VisitorCount.objects.get_or_create(pk=1)

    user_ip = get_client_ip(request)

    # unique visitor save
    VisitorIP.objects.get_or_create(ip_address=user_ip)

    # total views increase
    counter.total_views += 1
    counter.save()

    context = {
        'inf': inf,
        'total_views': counter.total_views,
        'unique_visitors': VisitorIP.objects.count(),
    }

    return render(request, 'bitbox/home.html', context)


def search_product(request):
    if request.method == "POST":
        query_phone = request.POST.get('searched')

        if query_phone:
            results1 = reg.objects.filter(phone__icontains=query_phone)
            results2 = bitboxc.objects.filter(phonenumber__icontains=query_phone)

            results = list(chain(results1, results2))  # combine

            return render(request, 'bitbox/search.html', {"results": results})

    return render(request, 'bitbox/search.html')

def user_support(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        SupportMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        return render(request, 'bitbox/support.html', {"success": True})

    return render(request, 'bitbox/support.html')

def get_client_ip(request):
    """ইউজারের আইপি অ্যাড্রেস বের করার ফাংশন"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
