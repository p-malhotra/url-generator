from flask import Flask, jsonify, request, json
from itertools import count
from threading import Thread
app = Flask('')

url_mapper = {
    "https://www.youtube.com/channel/UCHK4HD0ltu1-I212icLPt3g"
     : 'https://www.youtube.com/'
     ,
     "https://twitter.com/elonmusk?cn=ZmxleGlibGVfcmVjcw%3D%3D&":
      'https://twitter.com/elonmusk?cn=ZmxleGlibGVfcmVjcw%3D%3D&refsrc=email',
    "https://www.youtube.com/channel/UCHK4HD0ltu1-I212icLPt3g":
      'https://www.youtube.com/'
}

#generate increasing counter to be used to create tiny url
sequence = count(start=100000000, step=1)
counter = next(sequence)

def idToShortURL(id): 

    id = next(sequence)
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortURL = "" 
    # for each digit find the base 62 
    while(id > 0): 
        shortURL += map[id % 62] 
        id //= 62
  
    print("-*>",shortURL) 
    return shortURL[len(shortURL): : -1]+".ly" 

@app.route('/api/v1/links/generator', methods=['POST'])
def generate_url():
     data = request.json
     data = data['name']

    # Check if an name was provided as part of the payload.
    # If name is provided, generate short URL.
    # If no name is provided, display an error in the browser.     
     if data in url_mapper:
      return "Value for this key already exists."

     shortened = idToShortURL(counter) 
     url_mapper[data]= shortened

     return jsonify("data ->",shortened);

@app.route('/api/v1/links/search-tiny', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    
    results.append([k for k,v in url_mapper.items() if v == id])

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results) 

def run():
	app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()
