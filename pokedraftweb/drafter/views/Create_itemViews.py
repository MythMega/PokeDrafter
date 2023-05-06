from .dependancies import *

def create_player(request):
    template = loader.get_template('add/player.html')
    data = {}
    return HttpResponse(template.render(data, request))


def create_set(request):
    template = loader.get_template('add/set.html')
    data = {}
    return HttpResponse(template.render(data, request))