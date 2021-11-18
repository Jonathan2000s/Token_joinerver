import requests
#---index----
print("\033[1;35;40m Github https://github.com/Jonathan2000s \n")
link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)
#--Main--
print (link)
#Retrieve the token from the file and enter the serve
with open('token.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("Token has joined the server")
