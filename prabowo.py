from flask import Blueprint,render_template,redirect,url_for 

leadersound_for_prabowo = Blueprint('pb_route',__name__)

@leadersound_for_prabowo.route('/prabowo-route')
def prabowo():
    return f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>About Prabowo</title>
    <style>
      *, *::before, *::after {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }}
      body {{
        font-family: 'Segoe UI', system-ui, sans-serif;
        background: #f7f7f7;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
      }}
      .main {{
        background: #fff;
        border: 1px solid #e5e5e5;
        border-radius: 12px;
        padding: 2rem;
        width: 320px;
        text-align: center;
      }}
      .main-audio-content {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
      }}
      .audio-img img {{
        width: 130px;
        height: 130px;
        object-fit: cover;
        border-radius: 10px;
        border: 1px solid #e5e5e5;
      }}
      .audio-img img.playing {{
        animation: bob 0.5s ease-in-out infinite alternate;
      }}
      @keyframes bob {{
        from {{ transform: rotate(-1.5deg); }}
        to   {{ transform: rotate(1.5deg); }}
      }}
      h1 {{
        font-family: monospace;
        font-size: 15px;
        color: #111;
        margin-top: 0.75rem;
      }}
      p.sub {{
        font-size: 12px;
        color: #6b7280;
        margin-top: 4px;
      }}
      .btn {{
        margin-top: 0.25rem;
      }}
      .btn button {{
        background: darkwhite;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: opacity 0.15s;
      }}
      .btn button:hover {{ opacity: 0.8; }}
      .btn button:active {{ transform: scale(0.97); }}
      .btn button img {{ width: 20px; height: 20px; display: block; }} 

      .btn-reset button {{
  background: transparent;
  border: 1px solid #e5e5e5;
  border-radius: 8px;
  padding: 7px 20px;
  cursor: pointer;
  transition: background 0.15s;
}}
.btn-reset button:hover {{ background: #f7f7f7; }}
.btn-reset a {{
  font-size: 13px;
  color: #6b7280;
  text-decoration: none;
  font-family: 'Segoe UI', system-ui, sans-serif;
}}
.btn {{
  margin-top: 0.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}}
    </style>
   

  </head>
  <body>
    <div class="main">        
        <div class="main-audio-content">
           <audio id="audio">
              <source src="{url_for('static',filename="src/hidup-jokowi-sound/hidup-jokowi.mp3")}">  
           </audio>
           <div class="audio-img">
           <img src="{url_for('static',filename="src/hidup-jokowi-sound/prabowo-face/1.png")}" id="prabowo-image" alt="tester">  
           </div>
           <h1>Prabowo Subianto</h1>
            <p class="sub">Hidup Jokowi — LeaderSound</p>
        </div>
        

    <div class="btn">
      <button onclick="klik()">
        <img src="{url_for('static',filename="src/play.jpg")}" width="60px">
      </button>

      <div class="btn-reset">
      <button>
        <a href="{url_for('pb_route.prabowo')}">Reset</a>
      </button>
      </div>
     </div>
   
            
   


      <script src="{url_for('static',filename="js/hidup-jokowi.js")}"></script>

    
  </body>
</html>

    '''



