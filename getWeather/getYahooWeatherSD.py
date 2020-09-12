import urllib, pprint

api_endpoint = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Diego%2C%20ca%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")

#print 'URL: ', api_endpoint.geturl()
pp = pprint.PrettyPrinter(indent=4)

data = api_endpoint.read()

pp.pprint(data)
