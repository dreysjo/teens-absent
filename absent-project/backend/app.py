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
    return 'halo'

@app.route('/admin/login',methods=['POST','GET'])
def verify_admin():
    if request.method == 'POST':
        data = request.get_json()
        curr_username  = data['username']
        curr_password  = data['password']
        return jsonify(login_admin(curr_username,curr_password))
    return

@app.route('/student/recommendations', methods=['GET'])
def get_recommendations():
    data = get_all_jemaat()
    print(data)
    selected_keys = ['nama', 'id_jemaat']
    result_list = [{key: user[key] for key in selected_keys} for user in data]
    return jsonify(result_list)

@app.route('/student/login',methods=['POST','GET'])
def login_student():
    if request.method == 'POST':
        data = request.get_json()
        id_jemaat  = data['id_jemaat']
        login_time = datetime.now() 
        if add_absen(id_jemaat,login_time) ==  True:
            return jsonify({'status':f'success absen jemaat {id_jemaat}'})
    return jsonify({'status':'failed'})

if __name__ == '__main__':
    # initiate_table()
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    # print(login_student())
    app.run( port=5000, debug=1)
 
