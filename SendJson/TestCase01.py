import json
import datetime
import requests
import Properties
def sendingJson():
     now = datetime.datetime.now()
     NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
     f = open('data.json')
     t = open('template.json')
     dataTemplate = json.load(t)
     data = json.load (f)
     data['LloydsContractRef'] = dataTemplate['LloydsContractRef']
     data['UMR'] = dataTemplate['UMR']
     if dataTemplate['VersionUpdatedDate'] is None:
          data['VersionUpdatedDate'] = NVUD
     else:
          data['VersionUpdatedDate'] = dataTemplate['VersionUpdatedDate']
     data = json.dumps(data)
     writableFile = open('data.json','w')
     writableFile.write(data)
     writableFile.close()
     f.close()
     url = Properties.Url
     headers = Properties.Header
     return requests.post(url, files={'file': open('data.json', 'rb')},headers=headers) 



