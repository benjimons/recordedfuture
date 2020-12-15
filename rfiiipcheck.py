import urllib2
import json

token = 'TOKEN'
outputfile =  '/tmp/outputips.csv'

fw = open(outputfile, "a")

with open("ips.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for ip in content:
                url = "https://api.recordedfuture.com/v2/ip/"+ip+"?fields=risk"
                req = urllib2.Request(url, None, {'X-RFToken': token})
                fw.flush()
                try:
                        res = urllib2.urlopen(req)
                        response = json.loads(res.read())
                        fw.write(ip+","+response["data"]["risk"]["riskSummary"]+","+response["data"]["risk"]["criticalityLabel"]+"\r\n")
                except:
                        fw.write(ip+",not found\r\n")

fw.close()
