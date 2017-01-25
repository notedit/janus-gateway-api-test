# -*- coding: utf-8 -*-


import uuid
import json
import requests

transaction = uuid.uuid1().hex

data = {
        'janus':'create',
        'transaction':transaction
        }

req = requests.post('http://101.201.141.179:8088/janus',data=json.dumps(data))



ret = req.json()

print ret

#attach plugin


sessionid = ret['data']['id']


req = requests.post('http://101.201.141.179:8088/janus/' + str(sessionid), data=json.dumps({
        'janus':'attach',
        'transaction':transaction,
        'plugin':'janus.plugin.echotest'
        }))


print req.text


handle = req.json()


handleid =  handle['data']['id']


# destroy

"""
req = requests.post('http://101.201.141.179:8088/janus/' + str(sessionid), data=json.dumps({
        'janus':'destroy',
        'transaction':transaction,
        'plugin':'janus.plugin.echotest'
        }))


print req.text
"""

# handle endpoint



# yes  we send some message to the plugin


url = 'http://101.201.141.179:8088/janus/%s/%s/' % (str(sessionid),str(handleid))

req = requests.post(url, data=json.dumps({
        'janus':'message',
        'transaction':transaction,
        'body':{
            'audio':False
            }
    }))


print req.text
