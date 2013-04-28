from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.translation import force_text

# Lazy Serializer for dicts that have lazy strings like
# forms.errors...
class JSONLazyEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        else:
            return super(JSONLazyEncoder, self).default(obj)

class JsonResponse(HttpResponse):
    def __init__(self, object, fields=None, request=None):
        if isinstance(object, QuerySet):
            if fields is None:
                content = serialize('json', object)
            else:
                content = serialize('json', object, fields=fields)
        else:
            content = simplejson.dumps(object, cls=JSONLazyEncoder)
        if request is None:
            mimetype = 'application/json'
        elif 'application/json' in request.META['HTTP_ACCEPT_ENCODING']:
            mimetype = 'application/json'
        elif 'application/javascript' in request.META['HTTP_ACCEPT_ENCODING']:
            mimetype = 'application/javascript'
        else:
            mimetype = 'application/plain'
        super(JsonResponse, self).__init__(content, mimetype=mimetype)
