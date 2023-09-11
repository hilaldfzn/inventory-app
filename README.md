# **Inventory App**

**Tugas 2 - Pemrograman Berbasis Platform**

**Muhammad Hilal Darul Fauzan**<br/>
**2206830542**<br/>
**PBP C**<br/>

Link deployment untuk menuju aplikasi Inventory App dapat diakses melalui [Inventory App](https://inventory-app.adaptable.app/main/).

## **Membuat proyek Django baru**
1. Buat direktori baru dengan nama yang Anda pilih, contohnya `django_project` kemudian buka *command prompt* (Windows) atau *terminal shell* (Linux/Mac) di dalam direktori tersebut.
2. Buat *virtual environment* Python untuk mengisolasi proyek Python kita dengan menggunakan perintah `python -m venv env`.
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
7. Menambahkan `*` pada `ALLOWED_HOSTS` di dalam `settings.py` yang berada di dalam direktori `inventory_app` untuk mengizinkan akses dari semua host.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Kembali ke *command prompt* atau *terminal shell* dan jalankan server dengan perintah `python manage.py runserver` di dalam direktori proyek (pastikan ada file `manage.py` di sana). Lalu akses http://localhost:8000 di peramban web untuk melihat animasi roket yang menandakan bahwa aplikasi Django Anda telah berhasil dibuat.
9. Untuk menghentikan server, cukup dengan menekan tombol `Ctrl+C` di *command prompt* atau *terminal shell*. Pastikan juga untuk menonaktifkan *virtual environment* dengan menggunakan perintah `deactivate`.
10. Buat `.gitignore` yang berisi file yang tidak diperlukan agar tidak memenuhi space. Berikut adalah contoh isi dari `.gitignore`.
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
2. Buat aplikasi `main` dengan perintah `python manage.py startapp main`
3. Mendaftarkan aplikasi `main` ke proyek dengan menambahkan `'main'` pada `INSTALLED_APPS` di dalam file `settings.py`.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
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
* `description` sebagai deskripsi item dengan tipe `TextField`.<br/>
Dipersilakan untuk menambahkan atribut lainnya jika diinginkan, seperti `price`, `power`, `category`. Namun, model aplikasi Anda wajib memiliki ketiga atribut wajib di atas (`name`, `amount`, `description`).
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

> [!IMPORTANT]
> Setiap kali melakukan perubahan pada model, seperti menambahkan atau mengubah atribut, perlu melakukan migrasi untuk merefleksikan perubahan tersebut.

## **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML**
1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main` buat file `main.html` di dalamnya.
2. Buka file `views.py` pada direktori `main` dan tambahkan baris kode di paling atas `from django.shortcuts import render`. Ini akan mengimpor fungsi render dari modul django.shortcuts, yang akan digunakan untuk melakukan proses rendering tampilan HTML dengan menggunakan data yang diberikan.
3. Buat fungsi `show_inventory` dengan parameter `request`. Di dalam fungsi ini, buatlah sebuah dictionary `context` yang berisi data yang akan dikirimkan ke tampilan. Setelah itu, gunakan fungsi `render` dengan tiga argumen, yaitu `request` (objek permintaan HTTP yang dikirim oleh pengguna), nama file HTML yang akan digunakan untuk me-render tampilan, dan `context` (dictionary yang berisi data untuk digunakan dalam tampilan yang dinamis). Setelah itu, kembalikan hasil rendering tersebut.
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
4. Buka file `main.html` yang telah dibuat sebelumnya dan lakukan perubahan pada kode yang tadinya statis menjadi kode Django yang sesuai untuk menampilkan data. Gunakan sintaks Django `{{ }}` untuk memasukkan data dari `context` yang telah dikirimkan oleh fungsi `show_inventory`.

## **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**
Jika belum ada, buat file `urls.py` di dalam direktori main. Konfigurasi routing URL aplikasi `main` dengan melakukan perubahan pada file `urls.py` yang berada dalam direktori `main`.
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

## **Bonus**
Pada file `tests.py` buat testing tambahan selain yang diajarkan di tutorial.
```python
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_response_has_utf8_charset(self):
        response = Client().get('/main/')
        content_type = response.get('Content-Type', '')
        self.assertIn('utf-8', content_type.lower())
    
    def test_item_detail(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Katana')
        self.assertContains(response, 10)
        self.assertContains(response, 'Katana is a sword with a curved blade longer than 60 cm fitted with an uchigatana-style mounting and worn in a waist sash with the cutting edge facing up.')
        self.assertContains(response, 'Rp. 5000000,-')
        self.assertContains(response, '75')
        self.assertContains(response, 'Melee')
```


## **Bagan Client Request and Response - Django**
![alt-text](image/bagan.png)
Penjelasan bagan:
1. Client membuka browser untuk mengakses website.
2. Client memasuki website dan web server melayani request dari client.
3. WSGI memproses server HTTP untuk website berbasis Python.
4. Middleware berfungsi sebagai penghubung untuk mengintegrasikan teknologi yang digunakan dalam proyek untuk memproses request.
5. URL Router mengarahkan alamat proyek sesuai request dari client (urls.py), kemudian mengarahkannya ke fungsi yang ada di views.py.
6. Views (views.py) bertanggung jawab untuk merangkai konten yang akan ditampilkan dalam template HTML. Data yang diproses diambil dari basis data yang telah diorganisir menggunakan ORM dalam models.py.
7. Context processor mengirimkan data dari views.py ke template HTML.
8. Template HTML menampilkan tampilan depan proyek berdasarkan data konteks yang dikirimkan dari views.py dan mengikuti logika template tags.
9. Middleware berfungsi sebagai penghubung untuk mengintegrasikan teknologi yang digunakan dalam proyek untuk memproses response.
10. WSGI memproses server HTTP untuk website berbasis Python.
11. Web server melayani response dari server untuk dikirimkan ke client.
12. Client menerima response dari web server.

## **Mengapa kita perlu menggunakan *virtual environment*?**
*Virtual environment* diperlukan agar sistem dapat berjalan di lingkungan terisolasi. Di mana setiap proyek memiliki kebutuhan/dependensi yang berbeda-beda antara proyek satu dengan proyek yang lainnya. Dengan menggunakan *virtual environment*, maka proyek dapat berjalan sesuai dependensinya tanpa melakukan konfigurasi pada sistem operasi yang digunakan. File `requirements.txt` digunakan sebagai pencatatan daftar dependensi dari suatu proyek yang dijalankan dalam *virtual environment* tertentu. Hanya dengan mengetahui daftar dependensi yang ada melalui `requirements.txt` sebuah mesin host contohnya `Adaptable`, dapat mengetahui apa saja dependensi yang harus digunakan untuk menjalankan server. Hal ini juga memudahkan dalam proses penyimpanan di mana user tidak perlu melakukan push pada *virtual environment* karena sudah dicatat dengan baik di `requirements.txt` (*virtual environment* adalah direktori yang cukup memakan penyimpanan repository/host sehingga menghilangkannya dengan `.gitignore`).

## **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?**
Meskipun memungkinkan, namun tidak dianjurkan untuk membuat aplikasi web berbasis Django tanpa *virtual environment*, terutama jika Anda berencana untuk meng-hostnya secara online. Jika Anda hanya menjalankan proyek secara lokal di komputer Anda sendiri, mungkin bisa menggunakan environment Python bawaan (root) dan menginstal semua dependensi proyek di sana. Tetapi ketika Anda ingin meng-host aplikasi tersebut di layanan hosting online, seperti Adaptable, akan menjadi masalah. Server hosting akan mencari `requirements.txt` untuk mengetahui dependensi yang diperlukan. Jika tidak menggunakan *virtual environment* untuk mencatat dependensi ini, maka proyek Anda mungkin tidak akan berjalan dengan baik atau tidak berjalan sama sekali di lingkungan hosting tersebut. Oleh karena itu, sangat disarankan untuk menggunakan *virtual environment* dalam pengembangan aplikasi Django untuk memastikan kelancaran di berbagai lingkungan hosting.

## **Apa itu MVC, MVT, MVVM? Apa saja perbedaan dari ketiganya?**
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah kerangka kerja arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan berbagai komponen aplikasi dan membuatnya lebih terstruktur serta mudah dikelola. Meskipun mereka memiliki konsep dasar yang serupa dalam pembagian tugas, mereka digunakan dalam konteks yang berbeda dan memiliki perbedaan dalam pengorganisasian komponen-komponen tersebut.

### **MVC (Model-View-Controller)**
| **Model** | **View** | **Controller** |
| --- | --- | --- |
| Mengurus representasi data serta aturan bisnis dalam sebuah aplikasi. Bagian ini bertanggung jawab untuk mengakses dan mengelola data, baik yang berasal dari basis data atau sumber lainnya. Model juga merancang logika bisnis seperti validasi data dan perhitungan. Sebagai contoh, dalam pengembangan aplikasi e-commerce, model akan mengatur cara penyimpanan dan akses data terkait produk, pelanggan, dan pesanan. | Komponen yang mengurus tampilan yang diperlihatkan kepada pengguna. Ini adalah aspek yang terlihat oleh pengguna ketika mereka berinteraksi dengan aplikasi yang sedang kita kembangkan. Tugas utama dari View adalah untuk menampilkan data yang berasal dari Model ke layar. Misalnya, dalam konteks aplikasi e-commerce, View akan bertanggung jawab dalam menampilkan daftar produk dan rincian pesanan kepada pengguna. | Bagian yang berfungsi sebagai perantara antara Model dan View. Komponen ini mengontrol alur informasi dalam aplikasi. Controller bertanggung jawab untuk menangani permintaan yang diajukan oleh pengguna, mengolahnya, dan mengirimkannya ke Model untuk memperbarui data atau mengambil data yang diperlukan. Sebagai contoh dalam aplikasi e-commerce, jika pengguna menambahkan produk ke dalam keranjang belanja, Controller akan mengelola proses agar Model dapat menyimpan data tersebut dan selanjutnya memberi tahu View untuk memperbarui tampilannya. |
  
### **MVT (Model-View-Template)**
| **Model** | **View** | **Template** |
| --- | --- | --- |
| Mirip dengan MVC, dalam konsep MVT, Model adalah elemen yang bertugas mengorganisir dan mengelola data aplikasi. Model menggambarkan struktur data dan logika yang berada di latar belakang tampilan. Fungsinya mencakup penghubungan aplikasi dengan basis data dan mengatur cara interaksi dengan data tersebut. | Komponen yang mengelola logika tampilan dalam kerangka kerja MVT. View ini mengendalikan cara data yang dikelola oleh Model dipresentasikan kepada pengguna. Dalam konteks MVT, View berperan sebagai pengendali yang menampilkan data dan mengambilnya dari Model untuk kemudian disajikan kepada pengguna. | Komponen yang mengurusi tampilan pengguna, seperti halaman web. Dalam kerangka kerja seperti Django, Template digunakan untuk merancang antarmuka halaman web yang dinamis dan mengintegrasikan data dari Model sehingga pengguna dapat melihat informasi yang dipresentasikan melalui View. |

### **MVVM (Model-View-ViewModel)**
| **Model** | **View** | **ViewModel** |
| --- | --- | --- |
| Elemen yang mengatur data dan logika aplikasi, mirip dengan peran Model dalam kerangka kerja MVC dan MVT. Model dan ViewModel dalam MVVM akan bekerja bersama-sama untuk mengambil dan menyimpan data. | Komponen yang memperlihatkan antarmuka pengguna dan berfungsi untuk memberitahu ViewModel tentang tindakan yang dilakukan pengguna. Tetapi, dalam MVVM, View berperan sebagai penampil yang hanya menampilkan data dan tidak mengandung logika aplikasi apa pun. | Sebagai salah satu komponen kunci dalam MVVM, ViewModel berperan sebagai penghubung antara Model dan View. Tugasnya adalah mengubah data dari Model ke dalam format yang dapat disajikan oleh View dan mengelola logika tampilan. |


### **Perbedaan MVC, MVT, dan MVVM**
* #### **MVC**
    MVC adalah pola desain yang luasnya diterapkan dalam berbagai jenis aplikasi, termasuk desktop, web, dan mobile. Dalam MVC, Controller memainkan peran penting dalam mengatur aliran informasi antara Model dan View, meskipun ada situasi di mana Model dan View dapat berinteraksi langsung. Ini mengedepankan pemisahan tugas, dengan Model mengelola data dan logika bisnis, View menampilkan data, dan Controller mengelola aliran informasi. Namun, dalam MVC, pengembang sering harus secara manual mengurus pembaruan tampilan ketika data berubah, yang dapat memerlukan kode tambahan.

* #### **MVT**
    MVT adalah konsep yang khususnya digunakan dalam pengembangan web dengan kerangka kerja Django berbasis Python. Salah satu komponennya, yaitu Template (dalam MVT Django), mengkhususkan diri dalam mengatur tampilan halaman web, sementara Model dan View berperan serupa dengan MVC. Template adalah komponen tambahan yang tidak ada dalam MVC tradisional, dan Django memiliki alat bawaan untuk mengelola pembaruan tampilan secara otomatis saat data berubah.

* #### **MVVM**
    MVVM sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile atau desktop. Ini fokus pada pemisahan tugas tampilan dan logika dalam UI, dengan ViewModel bertindak sebagai penghubung antara Model dan View, mengurangi ketergantungan antara keduanya. MVVM menggunakan sistem pengikatan data (data binding) untuk otomatis memperbarui tampilan ketika data berubah di ViewModel. Meskipun ini mengurangi kode boilerplate untuk pembaruan tampilan, penggunaan data binding yang kompleks dapat membuat debugging aplikasi menjadi sedikit lebih rumit.