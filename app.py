from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def api():
   return jsonify({'message': 'otima API mano'})

@app.route("/user", methods=["GET"])
def user():
   return jsonify({'message': 'USER FOFO'})

@app.route("/news", methods=["PUT"])
def news():
   return jsonify({'message': 'NEWS GRANDE DEMAIS'})

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=3000, debug=True)