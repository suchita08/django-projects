from urllib.request import urlopen,Request
from urllib.parse import urlencode

user="BRIJESH"
key="ba24d737a5XX"
senderid="PRVRTN"
accusage="1"

def sendsms(mobile,message):
    values={
       'user':user,
        'key':key,
        'senderid':senderid,
        'mobile':mobile,
        'message':message,
        'accusage':accusage,

    }
    url="http://sms.bulkssms.com/submitsms.jsp"
    postdata=urlencode(values).encode("utf-8")
    req=Request(url,postdata)
    response=urlopen(req)
    response.read()