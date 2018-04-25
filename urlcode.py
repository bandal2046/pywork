import urllib2
import urllib

req = urllib2.Request('https://vshop.xiaokeduo.com/mid2948/did215157/Distributor')
try:
    urllib2.urlopen(req)
    print urllib2.urlopen(req).code,'OK?'
except urllib2.HTTPError, e:
    print e.code
    print e.reason
#except urllib2.URLError, e:

else:
    print "OK"
'''
url = 'https://vshop.xiaokeduo.com/mid2948/did215157/Distributo'
response = None
try:
  response = urllib2.urlopen(url,timeout=5)
except urllib2.URLError as e:
  if hasattr(e, 'code'):
    print 'Error code:',e.code
  elif hasattr(e, 'reason'):
    print 'Reason:',e.reason
finally:
  if response:
    response.close()
'''