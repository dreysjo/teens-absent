from flask import Blueprint, request, jsonify, flash
from .rmj_db import *
from werkzeug.security import generate_password_hash
auth = Blueprint('auth', __name__)


@auth.route('/admin/login',methods=['POST','GET'])
def verify_admin():
    if request.method == 'POST':
        data = request.get_json()
        curr_username  = data['username']
        curr_password  = data['password']
        return jsonify(login_admin(curr_username,curr_password))
    return

@auth.route('/student/login',methods=['POST','GET'])
def login_student():
    if request.method == 'POST':
        data = request.get_json()
        id_jemaat  = data['id_jemaat']
        login_time = datetime.now() 
        if add_absen(id_jemaat,login_time) ==  True:
            return jsonify({'status':f'success absen jemaat {id_jemaat}'})
    else:
        flash('Must be GET')
    return jsonify({'status':'failed'})

@auth.route('/student/create',methods=['POST','GET'])
def create_student():
    if request.method == 'POST':
        data = request.get_json()
        nama  = data['nama']
        no_telp  = data['no_telp']
        email  = data['email']
        gender  = data['gender']
        hobi  = data['hobi']
        sekolah  = data['sekolah']
        temp_lahir  = data['temp_lahir']
        tgl_lahir  = data['tgl_lahir']
        no_telp_ortu  = data['no_telp_ortu']
        kelas  = data['kelas']
        daerah  = data['daerah']
        kecamatan  = data['kecamatan']
        alamat  = data['alamat']
        foto  = data['foto']
        status  = data['status']
        return jsonify(add_jemaat(nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status))
    else:
        flash('Must be GET')
    return jsonify({'status':'failed'})

@auth.route('/admin/create',methods=['POST','GET'])
def create_admin():
    if request.method == 'POST':
        data = request.get_json()
        nama_admin  = data['nama_admin']
        password  = generate_password_hash(data['password'], method='sha256')
        last_login  = data['last_login']
        return jsonify(add_admin(nama_admin, password, last_login))
    #bisa redreict ke url

