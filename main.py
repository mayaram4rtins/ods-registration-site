from flask import Flask, render_template, request, flash, redirect
import json

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("html/Tela_de_login.html")

if __name__ == '__main__':
    app.run(debug=True)