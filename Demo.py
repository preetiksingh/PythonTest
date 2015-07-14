
import requests
import json
import urls   
import urllib2 
import csv
 


auth_url='http://uninstall.io/api/v1/auth/token'
application_url='http://uninstall.io/api/v1/applications'

def makerequests(_url,_name):
    r=requests.get(_url,headers=headers)
    return r


r= requests.post(urls.auth_url,data={"username":"findit","password":"findit"})
print "Token fetch status code", r.status_code

token = json.loads(r.text).get('token', '')
headers = {'Accept':'application/json','Authorization':'JWT '+token}

response = requests.get('http://uninstall.io/api/v1/applications',headers=headers)
print "Apps response:", response.status_code

apps = json.loads(response.text)
apps = apps.get('results', [])


api_urls = [
            {"name":"Chart_Counts","url":'http://uninstall.io/api/v1/charts/counts?app={app}'},
            {"name":"Uninstall_Counts","url":'http://uninstall.io/api/v1/charts/uninstalls?app={app}&start-date={start_date}&end-date={end_date}'},
            {"name":"Reinstall_Counts","url":'http://uninstall.io/api/v1/charts/reinstalls?app={app}&start-date={start_date}&end-date={end_date}'},
            {"name":"Event_Counts","url":'http://uninstall.io/api/v1/charts/events?app={app}&dimension=events&start-date={start_date}&end-date={end_date}'},
            {"name":"Source_Counts","url":'http://uninstall.io/api/v1/values/sources?app={app}'},
            {"name":"Device_Counts","url":'http://uninstall.io/api/v1/values/devices?app={app}'}
        ]

for url in api_urls:
    for a in apps:
        
        app_id= a['id']
        start_date='2015-06-06'
        end_date='2015-07-06'
        
        app_data = {
                    'app': app_id,
                    'start_date': start_date,
                                                     'end_date': end_date
                    }
        
        app_url = url.get('url').format(**app_data)
        url_response = makerequests(app_url, url.get('name'))
        json_response = json.loads(url_response.content)
        print json_response
        f = open('some.csv', 'wb')
        writer = csv.writer(f)
        
        if type(json_response) == type(dict()):
            for each in json_response:
                writer.writerow([json_response[each]])
        else:
            for each in json_response:         
                writer.writerow([each])
        
            
# with open("output.csv", "wb") as f:
    # writer = csv.writer(f)
    #writer.writerows(list)
     


        


    


#     

    
    
    
    
    
    
    
    
           
       
    
    
    


