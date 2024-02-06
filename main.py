import requests
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:

    url = "https://prod-191.westus.logic.azure.com:443/workflows/419d7c11a83d4491a42a8c56491cbc0e/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=no_msFm8FWDvTaRwnaZvrI904I3f0LSm0db-6yWNin8"
    data = {
        "input":"lol"
    }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)

    response =requests.post(url,headers=headers, data=json_data)

    print(response)