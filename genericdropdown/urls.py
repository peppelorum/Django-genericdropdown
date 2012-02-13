from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^updatecombo/(?P<id>\d+)?$', 'genericdropdown.views.updateCombo', name='updatecombo'),
)