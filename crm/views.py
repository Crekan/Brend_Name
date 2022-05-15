from django.shortcuts import render
from cms.models import CmsSlider
from .models import Order
from price.models import PriceTable, PriceCard
from .forms import OrderForm
from telebot.sendmessage import sendTelegram


def index(request):
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    slider_list = CmsSlider.objects.all()
    form = OrderForm()

    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form,
    }

    return render(request, 'index.html', dict_obj)


def thanks_page(request):
    if request.GET:
        name = request.GET['name']
        phone = request.GET['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        sendTelegram(tg_name = name, tg_phone = phone)
        return render(request, './thanks.html', {'name': name})
    else:
        return render(request, './thanks.html')
