from .dependancies import *


def index(request):
    template = loader.get_template('app/index.html')
    data = {}
    return HttpResponse(template.render(data, request))