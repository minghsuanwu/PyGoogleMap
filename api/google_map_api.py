'''
Created on 2017年11月13日

@author: Ming_Wu
'''
import googlemaps
import json

def test_simple_directions(origins, destinations, key):
    # Simplest directions request. Driving directions by default.
    client = googlemaps.Client(key)
    routes = client.directions(origins, destinations)
    printRoutes(routes)

def test_complex_request(origins, destinations, key):
    client = googlemaps.Client(key)
    routes = client.directions(origins, destinations,
                                   mode='driving',    #  'driving', 'walking', 'bicycling', 'transit'
#                                    avoid=['highways', 'tolls', 'ferries'],
                                   units='metric',
                                   region='tw')
    printRoutes(routes)

def google_map_api(origins, destinations, key):
    client = googlemaps.Client(key)
#     routes = client.directions(origins, destinations)

    routes = client.directions(origins, destinations,
                               mode='transit',
                               avoid=['highways', 'tolls', 'ferries'],
                               language='zh-TW',
                               units='metric',
                               region='tw')
    printRoutes(routes)

def printRoutes(json_string):
    temp = json.dumps(json_string)
    parsed_json = json.loads(temp)
    
    legs = parsed_json[0]['legs'][0]
    distance = legs['distance']['text']
    print('distance: '+distance)
    
    duration = legs['duration']['text']
    print('duration: '+duration)
    
    start_address = legs['start_address']
    print('start_address: '+start_address)
    
    end_address = legs['end_address']
    print('end_address: '+end_address)
    
    steps = legs['steps']
    print('\nSteps:')
    for index, step in enumerate(steps):
        print('Step'+str(index)+': ', steps[index]['html_instructions'].replace('<b>','').replace('</b>',''))
    
#     index = 0
#     for step in steps:
#         index += 1
#         print(step)

#     for i in range(len(steps)):
#         print('Step'+i+': '+steps[i]['html_instructions'])
    
    print()

def getConfig():
    data = json.load(open('client_secret.json'))
    return data['serverkey']

def main():
    key = getConfig()
    
    origins = '捷運關渡站'
    destinations = '捷運市政府站'
    google_map_api(origins, destinations, key)
#     test_simple_directions(origins, destinations, key)
#     test_complex_request(origins, destinations, key)

if __name__ == '__main__':
    main()
