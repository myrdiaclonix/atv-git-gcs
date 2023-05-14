from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/teste", methods=["POST"])
def teste():
   return jsonify({'message': 'otimo mano'})

@app.route("/foda", methods=["GET"])
def teste2():
   return jsonify({'message': 'FOFA'})

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)