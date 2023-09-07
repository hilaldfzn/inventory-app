<h1>Tugas 2 - Pemrograman Berbasis Platform</h1>

Muhammad Hilal Darul Fauzan
2206830542

Link Adaptable: https://inventory-app.adaptable.app

<h1>Mengapa perlu virtual environment?</h1>
Virtual environment diperlukan agar sistem dapat berjalan di lingkungan terisolasi. Di mana setiap proyek memiliki kebutuhan/dependensi yang berbeda-beda antara proyek satu dengan proyek yang lainnya. Dengan menggunakan virtual environment, maka proyek dapat berjalan sesuai dependensinya tanpa melakukan konfigurasi pada sistem operasi yang digunakan. File "requirements.txt" digunakan sebagai pencatatan daftar dependensi dari suatu proyek yang dijalankan dalam virtual environment tertentu. Hanya dengan mengetahui daftar dependensi yang ada melalui "requirements.txt" sebuah mesin host contohnya Adaptable, dapat mengetahui apa saja dependensi yang harus digunakan untuk menjalankan server. Hal ini juga memudahkan dalam proses penyimpanan di mana user tidak perlu melakukan push pada virtual environment karena sudah dicatat dengan baik di "requirements.txt" (virtual environment adalah directory yang cukup memakan penyimpanan repository/host sehingga menghilangkannya dengan .gitignore dapat merampingkan proyek)

<h1>Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</h1>
Meskipun memungkinkan, namun tidak dianjurkan untuk membuat aplikasi web berbasis Django tanpa virtual environment, terutama jika Anda berencana untuk meng-hostnya secara online. Jika Anda hanya menjalankan proyek secara lokal di komputer Anda sendiri, Anda mungkin bisa menggunakan environment Python bawaan (root) dan menginstal semua dependensi proyek di sana. Tetapi ketika Anda ingin meng-host aplikasi tersebut di layanan hosting online, seperti Adaptable, akan menjadi masalah. Server hosting akan mencari "requirements.txt" untuk mengetahui dependensi yang diperlukan, dan jika Anda tidak menggunakan virtual environment untuk mencatat dependensi ini, maka proyek Anda mungkin tidak akan berjalan dengan baik atau sama sekali di lingkungan hosting tersebut. Oleh karena itu, sangat disarankan untuk menggunakan virtual environment dalam pengembangan aplikasi Django untuk memastikan kelancaran di berbagai lingkungan hosting.

<h1>Apa itu MVC, MVT, MVVM? Apa saja perbedaan dari ketiganya?</h1>
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen-komponen yang berbeda dalam aplikasi agar lebih terstruktur dan mudah dikelola. Meskipun mereka memiliki kesamaan dalam memisahkan tugas-tugas, mereka digunakan dalam konteks yang berbeda dan memiliki perbedaan dalam cara mereka mengorganisasi komponen-komponen tersebut.
<br></br>

MVC (Model-View-Controller):
<ul>
  <li>Model: Mewakili data dan logika bisnis aplikasi. Ini berhubungan dengan pemrosesan data dan mengelola logika bisnis.</li>
  <li>View: Menampilkan data kepada pengguna dan mengatur tampilan aplikasi. Ini berhubungan dengan tampilan antarmuka pengguna.</li>
  <li>Controller: Menerima masukan dari pengguna, menginterpretasikan masukan tersebut, dan memutuskan tindakan yang akan diambil. Ini berhubungan dengan logika pengendalian aplikasi.</li>
</ul>
  
MVT (Model-View-Template):
<ul>
  <li>Model: Sama seperti dalam MVC, mewakili data dan logika bisnis aplikasi.</li>
  <li>View: Menampilkan data kepada pengguna. Namun, dalam konteks Django (kerangka kerja web Python yang menggunakan pola MVT), view juga mengatur alur logika presentasi.</li>
  <li>Template: Ini adalah komponen unik dari MVT yang mengontrol bagaimana data dari model akan ditampilkan dalam tampilan. Template digunakan untuk menghasilkan tampilan dinamis.</li>
</ul>

MVVM (Model-View-ViewModel):
<ul>
  <li>Model: Sama seperti dalam MVC dan MVT, mewakili data dan logika bisnis aplikasi.</li>
  <li>Menampilkan data kepada pengguna.</li>
  <li>Template: Ini adalah komponen unik dari MVT yang mengontrol bagaimana data dari model akan ditampilkan dalam tampilan. Template digunakan untuk menghasilkan tampilan dinamis.</li>
</ul>

--------------------------------------------PERBEDAAN UTAMA DARI MVC, MVT, MVVM---------------------------------------------
<ul>
  <li>MVC adalah pola arsitektur umum yang memisahkan model, view, dan controller.</li>
  <li>MVT adalah varian Django dari MVC dengan penekanan pada penggunaan template untuk mengatur tampilan.</li>
  <li>MVVM adalah pola yang biasanya digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna yang memerlukan tampilan yang dinamis, dengan ViewModel sebagai perantara antara model dan view.</li>
</ul>