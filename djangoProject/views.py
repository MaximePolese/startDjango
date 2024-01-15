import datetime

from django.http import HttpResponse, Http404


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, hours):
    try:
        hours = int(hours)
        min_hours = 1
        max_hours = 24
        if min_hours <= hours <= max_hours:
            dt = datetime.datetime.now() + datetime.timedelta(hours=hours)
            html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (hours, dt)
            return HttpResponse(html)
        else:
            raise Http404()
    except ValueError:
        raise Http404()

