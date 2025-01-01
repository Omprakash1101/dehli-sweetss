# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from .models import Category, Items
def index(request):
    items = Items.objects.filter(is_sold=False)[:]
    categories = Category.objects.all()[:]
    template = loader.get_template('templates/example/base.html')
    con={
        'items':items,
        'categories':categories,
 }
    return HttpResponse(template.render(con, request))