#import the request library that deals with headers
import requests
#introduce an error handler Try if the file doesn't exist
try:
    # open the file contains server list
    with open('ServerList.txt') as f:
        # iteratare through the file line by line
        for line in f.readlines():
            # for each iteration print each line and get request method and assign it to a variable in a dictionry format
            print(line.strip('\n'))
            r=requests.get(line.strip('\n'))
            #check with the first header
            if "deny" in r.headers ["X-Frame-Options"].lower():
                print(f" prevent all type of any clickjacking attacks")
            elif"sameorigin" in r.headers["x-frame-options"].lower():
                print(f'allow only same orgins frames')
            else:
                print(f'does not prevent all type of any clickjacking attacks')
            try:
                # check with the second header
                if "nosniff" in r.headers ["X-Content-Type-Options"].lower():
                    print(f"prevent the browser from MIME sniffing")
                # else:
                #     print(f" {line} doesn't the browser from MIME sniffing")
            except KeyError:
                print(f"-Content-Type-Options not found that means doesn't prevent MIME sniffing")
            # check with the third header
            try:
                if r.headers["Strict-Transport-Security"]:
                    print("Strict-Transport-Security", ':', "pass")
            except KeyError:
                print("Strict-Transport-Security header not present", ':', "fail!")
            print("\n")
except FileNotFoundError:
    print('There is no such file', f)




# #import the request library that deals with headers
# import requests
# #enable communication to the server using get request and assign the result to a variable
# r = requests.get('http://www.tomsguide.com/')
#
# #Define the required header as false boolean expressions
# if_server= False
# if_data = False
# if_connection =False
# if_connectionlength = False
# if_xconnectioncode = False
#
# #iterate through the results of get request and print the  key and values if key exists
# for key, val in r.headers.items():
#     if key.lower() == "server":
#         print(key, ':', val)
#         if_server = True
#     if key.lower() == "data":
#         print(key, ':', val)
#         if_data = True
#     if key.lower() == "connection":
#         print(key, ':', val)
#         if_connection = True
#     if key.lower() == "connection-length":
#         print(key, ':', val)
#         if_xconnectioncode = True
#     if key.lower() == "x-country-code":
#         print(key, ':', val)
#         if_connectionlength = True
#
# #if a header doesn't exist in the dictionary print not found for each header
# if if_server == False:
#     print("Server Header Not Fount")
# if if_connectionlength == False:
#     print("Connection Length Header Not Fount")
# if if_data == False:
#     print("Data Header Not Fount")
# if if_xconnectioncode == False:
#     print("X-Connection-Code Header Not Fount")
# if if_connectionlength == False:
#     print("Connection Length Header Not Fount")



# print (r.headers)
# new_headers = set(key.lower() for key in r.headers)
# print(new_headers)
#
# if all (key in new_headers for key in ('connection')):
#    print ('hello')
# else :
#    print ("hello112121")

# for header in r.headers:
#    if server or date or x-country-code or connection or connection-length in lower.header.values:
#       try:
#          result = r.headers[header]
#          print ('%s: %s' % (header, result))
#       except Exception as err:
#          print ('%s: No Details Found' % header)
#

