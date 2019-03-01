import sys
import requests
import subprocess



def get():
    #Need to install requests package for python
    #easy_install requests
    import sys
    import requests

    # Set the request parameters
    url = 'https://dev66195.service-now.com/api/now/table/incident/67295da6db3f2300095258b3ca96190a'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'Mechanics@565'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    sys.stdout = open('file', 'w')


    print(data)

    subprocess.call(['sh /var/lib/jenkins/workspace/postmethod-job/poll1.sh'])

    return
flag=1
#var =int(input("please enter a state value"))
while(flag<6):

#    if (var <6):
 #       flag=1

  #  else:
   #     flag=0


    get()
    
        
#if(var==6):
 #   print("incident resolved")

#else:


 #   while(True):

  #      get()




 


        
    

