import json, requests

'''
This function allows us to extract the information of the Foursquare API so that we can work with it. (It can be ised with other APIs)
Once the infromation has been extracted, it is treated so that we can work with the dictionary elements form the JSON object. 

The only argument required is the url that needs to be filled with the corresping parametres that can beo found in the developer manual.
'''

def extract(url):
    
    results = requests.get(url)
    
    code = json.loads(results.text)
    
    decoding = code.get("response")
    
    decoded = decoding.get("groups")[0]
    
    return decoded.get("items")