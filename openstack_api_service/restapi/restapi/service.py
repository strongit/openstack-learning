import os
import logging
import sys
from paste import deploy
from wsgiref.simple_server import make_server
import pdb

LOG = logging.getLogger(__name__)

module_dir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                        os.pardir,os.pardir))

sys.path.insert(0,module_dir) 

bind_host = "0.0.0.0"
bind_port = 8080

"""Provides ability to launch API from a 'paste' configuration."""
""" https://github.com/openstack/nova/blob/master/nova/service.py.WSGIService()"""

def server(app_name, conf_file):
    app = load_paste_app(app_name,conf_file) 
    serve = make_server(bind_host,bind_port,app) 
    serve.serve_forever() 

def load_paste_app(app_name, conf_file):
    LOG.debug("Loading %(app_name) from %(conf_file)",
                {'app_name':app_name, 'conf_file':conf_file})

    try:
        # pdb.set_trace()
        app = deploy.loadapp("config:%s" % os.path.abspath(conf_file), name=app_name)
        return app
    except (LookupError, ImportError) as e:
        LOG.error(str(e))
        raise RuntimeError(str(e))


if __name__ == '__main__':
    app_name = "restapi"
    conf_file = "paste-api.ini"
    server(app_name,conf_file)

