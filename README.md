# **Inventory App**

## **Tugas 2 - Pemrograman Berbasis Platform**

**Muhammad Hilal Darul Fauzan**<br/>
**2206830542**<br/>
**PBP C**<br/>

Link deployment untuk menuju aplikasi Inventory App dapat diakses melalui [Inventory App](https://inventory-app.adaptable.app).

## **Inisiasi sebuah proyek Django baru**
1. Buat direktori baru dengan nama yang Anda pilih, contohnya `django_project` kemudian buka *command prompt* (Windows) atau *terminal shell* (Linux/Mac) di dalam direktori tersebut.
2. Buat *virtual environment* python untuk mengisolasi proyek Python kita dengan menggunakan perintah `python -m venv env`.
3. Mengaktifkan *virtual environment* dengan perintah `env\Scripts\activate.bat` (Windows) atau `source env/bin/activate` (Linux/Mac). *Virtual environment* akan aktif dan ditandai dengan `(env)` di baris input terminal.
4. Buat file `requirements.txt` di dalam direktori proyek dan isi dengan daftar *dependencies* yang dibutuhkan untuk proyek Anda. Contoh beberapa *dependencies* yang akan digunakan sebagai berikut.
```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Install semua *dependencies* pada `requirements.txt` dengan perintah `python -m pip install -r requirements.txt`.
6. Buat proyek Django dengan nama `inventory_app` menggunakan perintah `django-admin startproject inventory_app .`.
7. Menambahkan `*` pada `ALLOWED_HOSTS` di dalam `settings.py` yang berada di dalam folder `inventory_app` untuk mengizinkan akses dari semua host.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Kembali ke *command prompt* atau *terminal shell* dan jalankan server dengan perintah `python manage.py runserver` di dalam direktori proyek (pastikan ada file `manage.py` di sana). Lalu akses http://localhost:8000 di peramban web untuk melihat animasi roket yang menandakan bahwa aplikasi Django Anda telah berhasil dibuat.
9. Untuk menghentikan server, cukup dengan menekan tombol `Ctrl+C` di *Command Prompt* atau *terminal shell*. Pastikan juga untuk menonaktifkan *virtual environment* dengan menggunakan perintah `deactivate`.
10. Buat `.gitignore` yang berisi file yang tidak diperlukan agar tidak memenuhi space.
```.gitignore
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

## **Membuat aplikasi dengan nama `main` pada proyek**
1. Buka *command prompt* pada direktori utama dan aktifkan *virtual environment* dengan perintah `env\Scripts\activate.bat`.
2. Membuat aplikasi `main` dengan perintah `python manage.py startapp main`
3. Mendaftarkan aplikasi `main` ke proyek dengan menambahkan `'main'` pada `INSTALLED_APPS` di dalam file `settings.py`.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
4. Buat direktori baru bername `templates` di dalam direktori aplikasi `main`. Di dalamnya, buat file `main.html` serta modifikasi dengan memasukan rancangan.
```html
<html>
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Inventory App Page</title>

      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

      <style>
        * {
          font-family: 'Poppins', sans-serif;
          cursor: pointer;
        }

        body {
          margin-top: 32px;
          text-align: center;
        }

        h1, h2, .profil, th, td {
          color: #333;
        }

        h1 {
          font-size: 36px;
          color: #25316D;
          margin-bottom: 10px;
        }

        h2 {
          font-size: 18px;
        }

        .profil {
          font-size: 16px;
        }

        .container-tabel {
          display: flex; 
          justify-content: center;
          background-color: #5F6F94;
          border-radius: 10px;
          padding: 20px;
          margin-top: 20px;
          box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        table {
          width: 100%;
        }

        .judul-tabel {
          background-color: #ffe4b5;
        }

        .judul-tabel th {
          font-weight: bold;
        }

        th, td {
          font-size: 16px;
          border: 1px solid black;
          padding: 10px 24px;
          font-weight: 400;
          border: 2px solid #25316D;
        }

        tr:nth-child(even) {
          background-color: white;
        }
      </style>
  </head>
  <body>
    <h1>Inventory App Page</h1>
    <h2>Tugas 2 - Pemrograman Berbasis Platform</h3>

    <div class="profil">
      <p>Nama: Muhammad Hilal Darul Fauzan</p>
      <p>NPM: 2206830542</p>
    </div>

    <div class="container-tabel">
      <table>
        <tr class="judul-tabel">
          <th>Name</th>
          <th>Amount</th>
          <th>Description</th>
          <th>Price</th>
          <th>Power</th>
          <th>Category</th>
        </tr>

        <tr>
            <th>{{ name }}</th>
            <th>{{ amount }}</th>
            <th>{{ description }}</th>
            <th>Rp. {{ price }},-</th>
            <th>{{ power }}</th>
            <th>{{ category }}</th>
        </tr>
      </table>
    </div>
  </body>
</html>
```
 
## **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**
Untuk menjalankan aplikasi yang dibuat perlu dilakukan konfigurasi routing proyek. Tambahkan path yang mengarah ke aplikasi tersebut di dalam file `urls.py` yang berada di dalam direktori proyek.
```python
"""
URL configuration for inventory_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```

## **Membuat model pada aplikasi `main`**
1. Pada langkah ini, ubah file `models.py` yang terdapat di dalam direktori aplikasi `main` untuk mendefinisikan model baru dengan nama `InventoryItem` dan memiliki atribut wajib sebagai berikut.
* `name` sebagai nama item dengan tipe `CharField`.
* `amount` sebagai jumlah item dengan tipe `IntegerField`.
* `description` sebagai deskripsi item dengan tipe `TextField`.

2. Isi file `models.py` dengan kode berikut.
```python
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.BigIntegerField()
    power = models.IntegerField()
    category = models.CharField(max_length=255)
```
3. Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi model lalu jalankan perintah `python manage.py migrate` untuk menerapkan migrasi ke dalam basis data lokal.

## **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML**
Integrasikan komponen MVT dengan melakukan modifikasi pada file `views.py` yang terletak dalam direktori `main`.
```python
from django.shortcuts import render

def show_inventory(request):
    context = {
        'name': 'Katana',
        'amount': 10,
        'description': 'Katana is a sword with a curved blade longer than 60 cm fitted with an uchigatana-style mounting and worn in a waist sash with the cutting edge facing up.',
        'price': 5000000,
        'power': 75,
        'category':'Melee'
    }

    return render(request, 'main.html', context)
```

## **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**
Konfigurasi routing URL aplikasi `main` dengan melakukan perubahan pada file `urls.py` yang berada dalam direktori `main`.
```python
from django.urls import path
from main.views import show_inventory

app_name = 'main'

urlpatterns = [
    path('', show_inventory, name='show_inventory'),
]
```

## **Melakukan deployment ke Adaptable**
1. Login [Adaptable.io](https://adaptable.io/) dengan menggunakan akun GitHub yang digunakan untuk membuat proyek.
2. Jika sudah login, silakan tekan tombol `New App`. Pilih `Connect an Existing Repository`.
3. Hubungkan [Adaptable.io](https://adaptable.io/) dengan GitHub dan pilih `All Repositories` pada proses instalasi.
4. Pilihlah repositori proyek aplikasi yang telah diunggah ke GitHub serta branch untuk deployment.
5. Pilihlah `Python App Template` sebagai template deployment.
6. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
7. Sesuaikan versi Python dengan spesifikasi aplikasimu. Untuk mengeceknya, nyalakan virtual environment dan jalankan perintah `python --version`.
8. Pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn (main directory).wsgi`.
9. Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
10. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi.

## **Client Request and Response - Django**

## **Mengapa kita perlu menggunakan *virtual environment*?**
*Virtual environment* diperlukan agar sistem dapat berjalan di lingkungan terisolasi. Di mana setiap proyek memiliki kebutuhan/dependensi yang berbeda-beda antara proyek satu dengan proyek yang lainnya. Dengan menggunakan *virtual environment*, maka proyek dapat berjalan sesuai dependensinya tanpa melakukan konfigurasi pada sistem operasi yang digunakan. File `requirements.txt` digunakan sebagai pencatatan daftar dependensi dari suatu proyek yang dijalankan dalam *virtual environment* tertentu. Hanya dengan mengetahui daftar dependensi yang ada melalui `requirements.txt` sebuah mesin host contohnya `Adaptable`, dapat mengetahui apa saja dependensi yang harus digunakan untuk menjalankan server. Hal ini juga memudahkan dalam proses penyimpanan di mana user tidak perlu melakukan push pada *virtual environment* karena sudah dicatat dengan baik di `requirements.txt` (*virtual environment* adalah direktori yang cukup memakan penyimpanan repository/host sehingga menghilangkannya dengan `.gitignore`).

## **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?**
Meskipun memungkinkan, namun tidak dianjurkan untuk membuat aplikasi web berbasis Django tanpa *virtual environment*, terutama jika Anda berencana untuk meng-hostnya secara online. Jika Anda hanya menjalankan proyek secara lokal di komputer Anda sendiri, Anda mungkin bisa menggunakan environment Python bawaan (root) dan menginstal semua dependensi proyek di sana. Tetapi ketika Anda ingin meng-host aplikasi tersebut di layanan hosting online, seperti Adaptable, akan menjadi masalah. Server hosting akan mencari `requirements.txt` untuk mengetahui dependensi yang diperlukan. Jika Anda tidak menggunakan *virtual environment* untuk mencatat dependensi ini, maka proyek Anda mungkin tidak akan berjalan dengan baik atau sama sekali di lingkungan hosting tersebut. Oleh karena itu, sangat disarankan untuk menggunakan *virtual environment* dalam pengembangan aplikasi Django untuk memastikan kelancaran di berbagai lingkungan hosting.

## **Apa itu MVC, MVT, MVVM? Apa saja perbedaan dari ketiganya?**
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen-komponen yang berbeda dalam aplikasi agar lebih terstruktur dan mudah dikelola. Meskipun mereka memiliki kesamaan dalam memisahkan tugas-tugas, mereka digunakan dalam konteks yang berbeda dan memiliki perbedaan dalam cara mereka mengorganisasi komponen-komponen tersebut.

### **MVC (Model-View-Controller)**
| **Model** | **View** | **Controller** |
| --- | --- | --- |
| Bertanggung jawab untuk mengelola dan pemrosesan data serta logika bisnis dalam aplikasi. | Menampilkan data kepada pengguna dan mengatur tampilan aplikasi. Ini berhubungan dengan tampilan antarmuka pengguna. | Berperan sebagai perantara antara Model dan View. Controller mengendalikan alur logika bisnis dan menerima input dari pengguna. |
  
### **MVT (Model-View-Template)**
| **Model** | **View** | **Template** |
| --- | --- | --- |
| Mirip dengan MVC, mengatur data dan logika bisnis. | Menampilkan data kepada pengguna. Namun, dalam konteks Django (kerangka kerja web Python yang menggunakan pola MVT), view juga mengatur alur logika presentasi. | Ini adalah komponen unik dari MVT yang mengontrol bagaimana data dari model akan ditampilkan dalam tampilan. Template digunakan untuk menghasilkan tampilan dinamis. |

### **MVVM (Model-View-ViewModel)**
| **Model** | **View** | **ViewModel** |
| --- | --- | --- |
| Sama dengan dalam MVC dan MVT, mengelola data dan logika bisnis. | Menampilkan tampilan kepada pengguna, tetapi dengan perbedaan bahwa View di MVVM lebih pasif dan hanya menampilkan data yang disediakan oleh ViewModel. | Bertindak sebagai perantara antara Model dan View. Ini mengelola data yang akan ditampilkan di View dan mengatur logika presentasi. |


### **Perbedaan MVC, MVT, dan MVVM**
* MVC adalah pola arsitektur umum yang memisahkan model, view, dan controller.
* MVT adalah varian Django dari MVC dengan penekanan pada penggunaan template untuk mengatur tampilan.
* MVVM adalah pola yang biasanya digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna yang memerlukan tampilan yang dinamis, dengan ViewModel sebagai perantara antara model dan view.