from . import db
from datetime import datetime
from sqlalchemy.sql import func

class Jemaat(db.Model):
    id_jemaat = db.Column('id_jemaat',db.Integer,primary_key=True)
    nama = db.Column('nama_jemaat',db.String(100))
    no_telp = db.Column('no_telp',db.String(100))
    email = db.Column('email',db.String(100), unique = True)
    gender = db.Column('gender',db.String(1))
    hobi = db.Column('hobi',db.String(100))
    sekolah = db.Column('nama_sekolah',db.String(100))
    temp_lahir = db.Column('tempat_lahir',db.String(100))
    tgl_lahir = db.Column('tanggal_lahir',db.DateTime)
    no_telp_ortu = db.Column('no_telp_ortu',db.String(100))
    kelas = db.Column('kelas',db.Integer)
    daerah = db.Column('daerah',db.String(100))
    kecamatan = db.Column('kecamatan',db.String(100))
    alamat = db.Column('alamat_lengkap',db.String(100))
    foto = db.Column('foto_jemaat',db.String(100))
    status = db.Column('status',db.String(100))
    absens = db.relationship('Absen')
    def __init__(self, nama, no_telp, email, gender, hobi, sekolah, temp_lahir, tgl_lahir, no_telp_ortu, kelas, daerah, kecamatan, alamat, foto, status):
        self.nama = nama
        self.no_telp = no_telp
        self.email = email
        self.gender = gender
        self.hobi = hobi
        self.sekolah = sekolah
        self.temp_lahir = temp_lahir
        self.tgl_lahir = tgl_lahir
        self.no_telp_ortu = no_telp_ortu
        self.kelas = kelas
        self.daerah = daerah
        self.kecamatan = kecamatan
        self.alamat = alamat
        self.foto = foto
        self.status = status

class Absen(db.Model):
    id_absen = db.Column('id_absen', db.Integer, primary_key=True)
    id_jemaat = db.Column('id_jemaat', db.Integer, db.ForeignKey('jemaat.id_jemaat'))
    waktu_absen = db.Column('waktu_absen', db.DateTime, default=func.now()) #, server_default=db.func.now()
    def __init__(self,id_jemaat, waktu_absen):
        self.id_jemaat = id_jemaat
        self.waktu_absen = waktu_absen

class Admin(db.Model):
    id_admin = db.Column('id_admin', db.Integer, primary_key=True)
    nama_admin = db.Column('nama_admin',db.String(100))
    password = db.Column('password',db.String(10))
    tanggal_terdaftar = db.Column('tanggal_terdaftar', db.DateTime, default = func.now())
    last_login = db.Column('last_login', db.DateTime, default = func.now())
    def __init__(self,nama_admin, password, last_login = func.now()):
        self.nama_admin = nama_admin
        self.password = password
        self.last_login = last_login