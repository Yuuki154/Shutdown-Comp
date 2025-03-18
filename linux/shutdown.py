from flask import Flask, render_template_string, request, abort, redirect, url_for
import os

app = Flask(__name__)

PASSWORD = "urosimalepuglavu"  # promeni sifru

@app.route('/')
def home():
    return render_template_string(''' 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Shutdown Control</title>
               <style>
                body {
                    background-color: black;
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                    
                }
                      
    button{
	box-shadow: 3px 4px 0px 0px #8a2a21;
	background:linear-gradient(to bottom, #c62d1f 5%, #f24437 100%);
	background-color:#c62d1f;
	border-radius:42px;
	border:4px solid #d02718;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:17px;
	padding:7px 53px;
	text-decoration:none;
	text-shadow:0px 1px 0px #810e05;
}
button:hover {
	background:linear-gradient(to bottom, #f24437 5%, #c62d1f 100%);
	background-color:#f24437;
}
button:active {
	position:relative;
	top:1px;}
    .first{
    font-size: 2rem;
    margin-top: 7%:}
            </style>
        </head>
        <body> <div class = "first">
            <h1>Ugasi komp :3</h1>
            <form action="/authenticate" method="post">
                <input type="password" name="password" placeholder="SIFRA MOLIM LEPO">
                <button type="submit">PRISTUP</button>
            </form>
            </div>
        </body>
        </html>
    ''')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.form['password'] != PASSWORD:
        abort(403)  
    return redirect(url_for('shutdown_page'))

@app.route('/shutdown-page')
def shutdown_page():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Shutdown Control</title>
               <style>
                body {
                    background-color: black;
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    font-family: Arial, sans-serif;
                    
                }
                      
    button{
	box-shadow: 3px 4px 0px 0px #8a2a21;
	background:linear-gradient(to bottom, #c62d1f 5%, #f24437 100%);
	background-color:#c62d1f;
	border-radius:42px;
	border:4px solid #d02718;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:17px;
	padding:7px 53px;
	text-decoration:none;
	text-shadow:0px 1px 0px #810e05;
}
button:hover {
	background:linear-gradient(to bottom, #f24437 5%, #c62d1f 100%);
	background-color:#f24437;
}
button:active {
	position:relative;
	top:1px;}
    .first{
    font-size: 2rem;
    margin-top: 7%:}
            </style>
        </head>
        <body>
        <div class = "first">
            <h1>JESI LI SIGURAN??????????</h1>
            <form action="/shutdown" method="post">
                <button type="submit">UGASI ME MOLIM TE</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.system('sudo shutdown -h now')  # Linux shutdown command
    return 'Shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
