from flask import Flask, render_template,request,session,redirect,url_for,flash,send_from_directory, jsonify
from .rmj_db import *
import os


from flask_cors import CORS
git 
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(APP_ROOT, 'images')
CORS(app)

@app.route('/',methods=['GET'])
def halo():
    return 'halo'

@app.route('/all-absent', methods=['POST','GET'])
def all_absen():
    return jsonify(get_all_absen())

@app.route('/filter-date-absent',methods=['POST','GET'])
def get_date_absen():
    if request.method == 'POST':
        data = request.get_json()
        date  = data['date']
    return jsonify(get_absen_by_date(date))

@app.route('/filter-name-absent',methods=['POST','GET'])
def get_name_absen():
    if request.method == 'POST':
        data = request.get_json()
        name  = data['name']
    return jsonify(get_absen_by_name(name))

@app.route('/filter-status-absent',methods=['POST','GET'])
def get_status_absen():
    if request.method == 'POST':
        data = request.get_json()
        status  = data['status'] #String [Active,Inactive]
    return jsonify(get_absen_by_status(status))

@app.route('/filter-absent-data', methods=['GET'])
def filter_absent_data():
    status = request.args.get('status')
    nama = request.args.get('nama')
    tanggal = request.args.get('tanggal')
    return jsonify(get_all_absen(status, nama, tanggal))
   

@app.route('/admin/login',methods=['POST','GET'])
def verify_admin():
    if request.method == 'POST':
        data = request.get_json()
        curr_username  = data['username']
        curr_password  = data['password']
        return jsonify(login_admin(curr_username,curr_password))
    return

@app.route('/student/create',methods=['POST','GET'])
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
    app.run( port=5000, debug=1)
 
