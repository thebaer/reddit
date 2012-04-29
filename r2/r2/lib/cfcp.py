#!/usr/bin/env python

import cloudfiles
from pylons import g

KEY_ID = g.CFKEY_ID
SECRET_KEY = g.CFSECRET_KEY

NEVER = 'Thu, 31 Dec 2037 23:59:59 GMT'

def send_file(container, filename, content, content_type = 'text/plain', never_expire = False, replace=False, reduced_redundancy=False):

    connection = cloudfiles.get_connection(username=KEY_ID, api_key=SECRET_KEY)
    container = connection.get_container(container)
    o = container.create_object(filename)
    o.content_type = content_type
    o.send(content)


