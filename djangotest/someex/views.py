import datetime
from django.http import HttpResponse

# Create your views here.


def index(request):
    html = "<html><body>Какой-то текст<BR><h1>Еще текст</h1></body></html>"
    return HttpResponse(html)

