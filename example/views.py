# example/views.py
from datetime import datetime
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('example/base.html')
    con={
    'now':datetime.now(),
    'html':f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is .</p>
        </body>
    </html>
    ''',}
    return HttpResponse(template.render(con, request))