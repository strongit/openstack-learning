import httplib
import json
import webob.dec

from webob import Response

class ServersController(object):
    
    """The Server API base controller class for the OpenStack API."""

    def __init__(self):
        # TODO
        self.version = "0.1"
        self.hello = "Hello World"

    def index(self,req):
        response = Response(request=req,
                                  status=httplib.MULTIPLE_CHOICES,
                                  content_type='application/json')
        response.body = json.dumps(dict(versions=self.version))
        return response

    def greet(self,req):
        response = Response(request=req,
                                  status=httplib.MULTIPLE_CHOICES,
                                  content_type='application/json')
        response.body = json.dumps(dict(versions=self.hello))
        return response

    @webob.dec.wsgify
    def __call__(self, req):
        # TODO
        return self.index(req)
        # results = map.routematch(environ=req.environ)
        # if not results:
        #     return webob.exc.HTTPNotFound()
        # match, route = results
        # link = routes.URLGenerator(self.map, req.environ)
        # req.urlvars = ((), match)
        # kwargs = match.copy()
        # method = kwargs.pop('method')
        # req.link = link
        # return getattr(self, method)(req, **kwargs)

def create_resource():
    return ServersController()

#https://github.com/openstack/nova/blob/master/nova/api/openstack/compute/servers.py