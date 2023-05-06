from .dependancies import *

def start_draft(request):
    template = loader.get_template('draft/new.html')
    data = {}
    return HttpResponse(template.render(data, request))
