from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('backend.views',
    
    url(r'^$', 'index'),
)
