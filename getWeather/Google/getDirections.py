import requests

r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=12840+Orangeburg+Ave+San+Diego,+CA&destination=4810+Eastgate+Mall+San+Diego,+CA+92121&waypoints=optimize:true|9225+Adolphia+Street+San+Diego,+CA+92129|13340+Hayford+Way+San+Diego,CA+92130|&key=AIzaSyC_U8bu60yw_joL9UjBSaKSzB9U7hQd7UM')

response = r.json()

for leg in response['routes'][0]['legs']:
    print ('Start address: '+leg['start_address'])
    print ('End address: '+leg['end_address'] +'\n')

for step in response['routes'][0]['legs'][0]['steps']:
            print (step['html_instructions'])