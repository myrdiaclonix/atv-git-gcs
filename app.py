from flask import Flask, request, jsonify
import random
app = Flask(__name__)

def somaAleatoria():
   return random.randint(1, 10)

def randomDogBreed():
   breeds = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog", "Bulldog", "Poodle", "Beagle", "Dachshund", "Rottweiler", "Yorkshire Terrier"]
   return random.choice(breeds)

def readFile(path):
   f = open(path, "r")
   archive = f.read()
   f.close()
   return archive

@app.route("/api-teste", methods=["POST"])
def api():
   file = readFile("arquivo.txt")
   return jsonify({'message': f'otima API mano que legal uhulll {randomDogBreed()}, {file}'})

@app.route("/user", methods=["GET"])
def user():
   return jsonify({'message': [f'USER FOFO {somaAleatoria()}', 'lembre de piscar 👀']})

@app.route("/news", methods=["PUT"])
def news():
   return jsonify({'message': 'NEWS GRANDE DEMAIS, se está doido, festa semana que vem ein'})

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=3333, debug=True)