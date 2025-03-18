from flask import Flask, render_template_string, request, abort, redirect, url_for
import os

app = Flask(__name__)


PASSWORD = "urosuki"  

@app.route('/')
def home():
    return render_template_string(''' 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Shutdown Control</title>
        </head>
        <body>
            <h1>Ugasi komp :3</h1>
            <form action="/authenticate" method="post">
                <input type="password" name="password" placeholder="SIFRA MOLIM LEPO">
                <button type="submit">PRISTUP</button>
            </form>
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
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
                button {
                    background-color: purple;
                    color: white;
                    font-size: 30px;
                    padding: 20px 40px;
                    border: none;
                    cursor: pointer;
                    border-radius: 10px;
                }
                button:hover {
                    background-color: darkviolet;
                }
            </style>
        </head>
        <body>
            <h1>JESI LI SIGURAN??????????</h1>
            <form action="/shutdown" method="post">
                <button type="submit">UGASI ME MOLIM TE</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.system('shutdown /s /f /t 0') 
    return 'Shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
