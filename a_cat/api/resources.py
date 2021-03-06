from django.conf import settings
# from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
# from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import CharField  #ToManyField, ToOneField
from tastypie.resources import ModelResource, Resource
from a_cat.models import Image, Post, CatOff

# insert Resource(ModelResource) files


class ImageResource(ModelResource):  # this connects to models.py through a "from...import..."
    class Meta:
        queryset = Image.objects.all()
        resource_name = "image"


class PostResource(ModelResource):  # this connects to models.py through a "from...import..."
    class Meta:
        queryset = Post.objects.all()
        resource_name = "post"


class CatOffResource(ModelResource):  # this connects to models.py through a "from...import..."
    class Meta:
        queryset = CatOff.objects.all()
        resource_name = "catoff"



######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)