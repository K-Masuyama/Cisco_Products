import json
import requests
import time
requests.packages.urllib3.disable_warnings()


def post_method(url, header, params=None):
    try:
        request = requests.post(
            url = url,
            verify = False,
            headers = header,
            data = json.dumps(params)
            )
        return json.loads(request.content)
    except requests.exceptions.RequestException as e:
        print(e)

# Need To Fill
api_key = ""
ACCESS_TOKEN = ""
room_id = ""


meraki_url = "https://api.meraki.com/api/v0/networks/L_669347494617944255/cameras/Q2EV-GFCE-Y32U/snapshot"
meraki_header = {'X-Cisco-Meraki-API-Key': api_key}

resp = post_method(meraki_url, meraki_header)

accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
teams_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
teams_url = "https://api.ciscospark.com/v1/messages"


params_1 = {
    "roomId" : room_id,
    "markdown" : resp["expiry"],
    "files" : resp["url"]
}
params_2 = {
    "roomId" : room_id,
    "markdown" : resp["url"]
}
time.sleep(5)
resp_teams_1 = post_method(teams_url, teams_header, params_1)
resp_teams_2 = post_method(teams_url, teams_header, params_2)
