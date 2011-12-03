from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('backend.views',
    
    url(r'^$', 'get_classmates'),
    # url(r'^classmates/$', 'get_classmates'),
)
