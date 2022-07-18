import requests
Endpoint = "https://brill.live.bhvrdbd.com/api"  # Epic games

async def Request(type, method, session=None, headers=None, data=None):
    
    match type:
        case "POST":
            call = requests.post
        case "GET":
            call = requests.get

    req = call(url=f"{Endpoint}{method}", headers=headers, cookies=session, data=data, verify=True).content.decode()
    return req
