from flask import Flask, render_template,request,session,redirect,url_for,flash,send_from_directory, jsonify
from rmj_db import *
import socket
import os
import random
import string

from flask_cors import CORS

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(APP_ROOT, 'images')
CORS(app)

@app.route('/',methods=['GET'])
def halo():
    # print("hello")
    return 'halo'

@app.route('/admin/login',methods=['POST','GET'])
def verify_admin():
    # print("hello")
    if request.method == 'POST':
        # print('hello2')
        data = request.get_json()
        # print(data)
        # print(data['username'])
        curr_username  = data['username']
        curr_password  = data['password']
        return jsonify(login_admin(curr_username,curr_password))
    return

@app.route('/student/login',methods=['POST','GET'])
def login_student():
    # print("hello")
    if request.method == 'POST':
        # print('hello2')
        data = request.get_json()
        # print(data)
        # print(data['username'])
        curr_username  = data['name']
        login_time = datetime.now()
        return jsonify(add_absen(curr_username,login_time))
    return

if __name__ == '__main__':
    # initiate_table()
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    app.run( port=5000, debug=True)


