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
        id_jemaat  = data['id_jemaat']
        login_time = datetime.now()
        return jsonify(add_absen(id_jemaat,login_time))
    return jsonify({'status':'failed'})

@app.route('/regristration',methods=['POST','GET'])
def student_regristration():
    if request.method == 'POST':
        data = request.get_json()
        nama = data['nama']
        no_telp = data['no_telp']
        email = data['email']
        gender = data['gender']
        hobi = data['hobi']
        sekolah = data['sekolah']
        temp_lahir = data['temp_lahir']
        tgl_lahir = data['tgl_lahir']
        no_telp_ortu = data['no_telp_ortu']
        kelas = data['kelas']
        daerah = data['daerah']
        kecamatan = data['kecamatan']
        alamat = data['alamat']
        foto = data['foto']
        status = data['status']
        return jsonify(add_jemaat(nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status))
    return jsonify({'status':'failed'})

if __name__ == '__main__':
    # initiate_table()
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    app.run(port=5000, debug=True)


