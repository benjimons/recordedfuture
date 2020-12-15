import urllib2
import json

token = 'TOKEN'
outputfile =  '/tmp/outputdomains.csv'

fw = open(outputfile, "a")

with open("domains.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for domain in content:
                url = "https://api.recordedfuture.com/v2/domain/"+domain+"?fields=risk"
                req = urllib2.Request(url, None, {'X-RFToken': token})
                fw.flush()
                try:
                        res = urllib2.urlopen(req)
                        response = json.loads(res.read())
                        fw.write(domain+","+response["data"]["risk"]["riskSummary"]+","+response["data"]["risk"]["criticalityLabel"]+"\r\n")
                except:
                        fw.write(domain+",not found\r\n")

fw.close()
