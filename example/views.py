# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('templates/example/base.html')
    con={
'now':datetime.now(),
 }
    return HttpResponse(template.render(con, request))