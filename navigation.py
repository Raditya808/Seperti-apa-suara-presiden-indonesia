from flask import Flask,render_template,redirect,url_for
from prabowo import leadersound_for_prabowo
from jokowi import leadersound_for_jokowi

app = Flask(__name__)
app.register_blueprint(leadersound_for_prabowo) 
app.register_blueprint(leadersound_for_jokowi)



@app.route('/')
def home():
    return f'''
    <!DOCTYPE html> 
    <html>
        <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>About Leader</title>
    <style>
        a{{
        text-decoration: none;
        }}
    </style>
        </head>
        <body>
            <div class="main">
                <h1>What's Indonesian Leader Sounds Like?</h1>
                <div class="navigation">
                <ul>
                
                   <li><a href="{url_for('pb_route.prabowo')}">Prabowo sound</a></li> 
                   <li><a href="{url_for('jk-route.jokowi')}">Jokowi sound</a></li>
                   
                </ul>
                </div>
           </div>
        </body>
    </html> 
    '''


