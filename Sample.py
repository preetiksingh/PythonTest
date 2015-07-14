

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

httpServ = httplib.HTTPConnection("127.0.0.1", 80)
httpServ.connect()

quote = "test"
httpServ.request('POST', '/cgi_form.cgi', 'name=Brad&quote=%s' % quote)

response = httpServ.getresponse()
if response.status == httplib.OK:
    print "Output from CGI request"
    printText (response.read())

httpServ.close()
