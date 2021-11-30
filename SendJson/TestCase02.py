import requests.api
import Properties
import json
import datetime
import requests
def emptyUMR():
    now = datetime.datetime.now()
    NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    f = open('data.json')
    t = open ('template.json')
    dataTemplate = json.load(t)
    data = json.load (f)
    data['LloydsContractRef'] = dataTemplate['LloydsContractRef']
    data['UMR'] = dataTemplate['UMR']
    data['VersionUpdatedDate'] = NVUD
    data = json.dumps(data)
    writableFile = open('data.json','w')
    writableFile.write(data)
    writableFile.close()
    f.close()
    url = Properties.Url
    headers = Properties.Header
    return requests.post(url, files={'file': open('data.json', 'rb')},headers=headers) 
print('hola javi')

