# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Import the requests module to handle HTTP requests
import requests

# Define a function to fetch Pokémon data from the Pokémon API
def get_pokemon_data():
    # Send a GET request to the Pokémon API to fetch data
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
    # Convert the response to JSON format
    data = response.json()
    # Return the results from the JSON data
    return data['results']

# Define a route for the root URL ('/')
# When users visit the root URL, the index() function will be called
@app.route('/')
def index():
    # Call the function to get Pokémon data
    pokemon_data = get_pokemon_data()
    # Render the HTML template 'index.html' and return it to the user
    return render_template('index.html', pokemon=pokemon_data)

# Check if the script is run directly (not imported)
# If so, run the app with debug mode enabled (useful for development)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)