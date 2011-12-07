Genericdropdown is a small little nifty script that removes the obstacle of picking the right object when using generic relations in Django. The script replaces the input field for the object id with a dropdown instead.


Howto use
--------
Just add the url to your url config and you should be fine, and add a line to your template directory setting as well

    url(r'^', include('genericdropdown.urls')),
    
    TEMPLATE_DIRS = (
       'templates/',
       'genericdropdown/templates'
   )
