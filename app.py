# https://www.youtube.com/watch?v=dfeM91JG3oQ
# Automatic deployment on push of any application to VPS server by using Github workflows action https://www.youtube.com/watch?v=V2YYhGn3MGo
from flask import Flask, jsonify
app=Flask(__name__)

@app.route("/")
def root():
    return jsonify({"Message":"Hello from Flask!! oh yeah"})

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
