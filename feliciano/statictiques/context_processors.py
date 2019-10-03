import requests
import json
from . import models
def visitor_ip_address(request):

    ip=request.client_ip
    if ip=='127.0.0.1':
        req = requests.get('https://api.ipify.org?format=json')
        data = json.loads(req.text)
        ip = data['ip']
    print(ip)
    url = "https://ipapi.com/ip_api.php?ip={}"
    try:
        req = requests.get(url.format(ip))
        if req.status_code:
            data = json.loads(req.text)
            latitude = data['latitude']
            longitude = data['longitude']
            pays = data['country_name']
            ville = data['city']
            continent = data['continent_name']
            reseau = data['connection']['isp']
            client = models.Client(
                ip=ip,
                pays=pays,
                ville=ville,
                continent=continent,
                reseau=reseau,
                latitude=latitude,
                longitude=longitude
            )
            client.save()
    except :
        print('error')
    return {'ip':ip}


