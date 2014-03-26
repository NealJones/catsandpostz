from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from a_cat.api.resources import ImageResource, PostResource, CatOffResource
from django.conf import settings

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(ImageResource())  # connects to resources.py - must be imported
v1_api.register(PostResource())  # connects to resources.py - must be imported
v1_api.register(CatOffResource())  # connects to resources.py - must be imported


urlpatterns = patterns('',
    url(r'^$', 'a_cat.views.angular', name="angular"),

    url(r'^a_cat/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^api/', include(v1_api.urls)),

    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),


    url(r'^fbpost/', 'a_cat.views.get_fb_post', name="fb_post"),

)


# http://127.0.0.1:8000/api/v1/image/?format=json
## - This is currently working 20140313 17:09

