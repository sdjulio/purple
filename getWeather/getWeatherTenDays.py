import requests

HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
deg = deg = u"\u00B0"


def get_data(url):
    response = requests.get(url, params=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.text)
        print(response.status_code)


for i in range(1):
    api_url = 'https://query.yahooapis.com/v1/public/yql?q='
    query = 'select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Diego%2C%20ca%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"'
    weatherUrl = api_url + str(query)
    response = get_data(weatherUrl)

    for elem in response['query']['results']['channel']['item']['forecast']:
        #Print syntax is specific to Python 2.
        #Python 3 uses different syntax.
        print ("Date: " + elem['date'])
        print ("Conditions: " + elem['text'])
        print ("High: " + elem['high'] + " " + deg + "F")
        print ("Low: " + elem['low'] + " " + deg + "F\n")
