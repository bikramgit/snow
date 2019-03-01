import sys
import requests
import subprocess


def get():
    #Need to install requests package for python
    #easy_install requests
    import sys
    import requests

    # Set the request parameters
    url = 'https://dev66195.service-now.com/api/now/table/incident/dfbff713db332300095258b3ca961971'

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


  #  print("hii i'm back")

    sys.stdout=open("file1234","w")
    #sys.stdout=open("filexyz","w")
    print(data)
    
    #with open("file123", "w+") as f:
        
   # print("i'm here")
     #   f=open("file123","w+")
      #  f.close()
    
    #print("printing again")
    #print("ok got it")

    #f.close()
    

    return
#print("i'm inside the python file")
#print(sys.argv[1])
#print("done-it")
#i =int(input("please enter a state value"))
#i=sys.argv[1]

#print(i,"i value changed")
#k=i
#print(k,"same as i")

#j=1
#while(j<7):
 #   print("i'm inside loop")
  #  get()
   # i +=2
    print ("hi i'm in while-loop")
    
   # subprocess.call(['/var/lib/jenkins/workspace/postmethod-job/poll2.sh'])

    #subprocess.call(['/var/lib/jenkins/workspace/postmethod-job/xyz.sh'])

    #i=sys.argv[1]
    #j=i
get()




#while(True):
    #get()
        
#if(var==6):
 #   print("incident resolved")

#else:


 #   while(True):

  #      get()

