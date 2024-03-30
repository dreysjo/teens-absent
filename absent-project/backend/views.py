from flask import Blueprint, request, jsonify, flash
from .rmj_db import *

views = Blueprint('views', __name__)

@views.route('/',methods=['GET'])
def halo():
    return '<h1>halo</h1>'

@views.route('/all-absent',methods=['POST','GET'])
def all_absen():
    return jsonify(get_all_absen())

@views.route('/filter-date-absent',methods=['POST','GET'])
def get_date_absen():
    if request.method == 'POST':
        data = request.get_json()
        date  = data['date']
    return jsonify(get_absen_by_date(date))

@views.route('/filter-name-absent',methods=['POST','GET'])
def get_name_absen():
    if request.method == 'POST':
        data = request.get_json()
        name  = data['name']
    return jsonify(get_absen_by_name(name))

@views.route('/filter-status-absent',methods=['POST','GET'])
def get_status_absen():
    if request.method == 'POST':
        data = request.get_json()
        status  = data['status'] #String [Active,Inactive]
    return jsonify(get_absen_by_status(status))

@views.route('/edit-data-jemaat',methods=['POST','GET'])
def edit_status_jemaat():
    if request.method == 'POST':
        data = request.get_json()
        id_jemaat  = data['id_jemaat']
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
        status  = data['status'] #String [Active,Inactive]
    return jsonify(edit_data_jemaat(id_jemaat, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status))

