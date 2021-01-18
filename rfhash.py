import urllib2
import json
import sys
import hashlib
import os

token = 'TOKEN'
outputfile =  '/tmp/outputhashesnew.csv'
BUF_SIZE = 65536 

def rfcheck(hash):	
	url = "https://api.recordedfuture.com/v2/hash/"+hash+"?fields=risk"
	req = urllib2.Request(url, None, {'X-RFToken': token})
	try: 
		res = urllib2.urlopen(req)
		response1 = json.loads(res.read())
		response = response1["data"]["risk"]["riskSummary"]+","+response1["data"]["risk"]["criticalityLabel"]
	except:
		response = "not found"

	return response

if __name__ == '__main__':  
   mypath = sys.argv[1]  
   myfiles = []
   fw = open(outputfile, "a")
   i=0

   for root, dirs, files in os.walk(mypath):
    for file in files:
        myfiles.append(os.path.join(root, file))
   totalfiles = len(myfiles)
   
   for x in myfiles:
     i += 1
	  md5 = hashlib.md5()
	  with open(x, 'rb') as f:
		  filesize = os.path.getsize(x)
		  print("Hashing "+x+" filesize "+str(filesize))
		  while True:
        		data = f.read(BUF_SIZE)
        		if not data:
            			break
	        	md5.update(data)
		  print("Checking against RF MD5: {0}".format(md5.hexdigest()))
		  output = x+","+format(md5.hexdigest())+","+str(rfcheck(format(md5.hexdigest())))+"\r\n"
                fw.write(output)
		  fw.flush()
		  print(output)
		  del data
	  print("Completed: "+str(i)+"/"+str(totalfiles))
