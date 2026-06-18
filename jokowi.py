from flask import Blueprint,url_for


leadersound_for_jokowi = Blueprint('jk-route',__name__)


@leadersound_for_jokowi.route('/jokowi-route')
def jokowi():
    return f'''
<!DOCTYPE html>
<html lang="en">
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>About Jokowi</title>
    
 </head>
 </html>
    '''
