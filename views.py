from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType


def updateCombo(request, id):
    model_class = ContentType.objects.get(id=id).model_class()

#    print "appa", model_class

    a = model_class.objects.all()
    out = ""
    for b in a:
        out = "%s<option value='%s'>%s" % (out, unicode(b.id), b,)
    out = "<option></option>"+ out
    return HttpResponse(out)

