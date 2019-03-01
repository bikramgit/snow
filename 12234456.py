import sys
import requests



def get():
    #Need to install requests package for python
    #easy_install requests
    import sys
    import requests

    # Set the request parameters
    url = 'https://dev66195.service-now.com/api/now/table/incident/55b849efdbb32300095258b3ca961980'

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


#    print("hii i'm back")

    sys.stdout=open("file1234","w")

    print(data)
    
    #with open("file123", "w+") as f:
        
   # print("i'm here")
     #   f=open("file123","w+")
      #  f.close()
    
  #  print("printing again")
 #   print("ok got it")

    #f.close()
    

    return

i =int(input("please enter a state value"))

while(i<6):
    #if (var <6):
     #   flag=1
    #else:
     #   flag=0
    get()
    i +=2






#while(True):
    #get()
        
#if(var==6):
 #   print("incident resolved")

#else:


 #   while(True):

  #      get()



