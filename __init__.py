from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__) 
def hello_world():
    return render_template('hello.html')
                                                                                                                                       
@app.route('/')
<pre><code><xmp>
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact est</h2>"
</xmp></code></pre>

def hello_world():
    return render_template('hello.html')
  
if __name__ == "__main__":
  app.run(debug=True)
