Khansa Mahira
2206819413
PBP D

**Tugas 2**

**Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).**
Jawaban:
1)  Saat membuat aplikasi Django, saya memulai dari membuat direktori bernama library yang saya inisialisasikan dengan github.
2)  Berikutnya saya membuat repositori bernama library di github untuk menyimpan direktori aplikasi secara virtual.
3)  Pada direktori library di komputer saya, saya membuat dan mengaktifkan _environment_ Django dengan memanfaatkan isi dari requirements.txt sehingga memudahkan saya tanpa perlu menyusun kode aplikasi dari awal.
4)  Selanjutnya, saya membuat aplikasi main. Setelah dibuat direktori main, maka pada settings.py dalam direktori library saya menambahkan main pada list INSTALLED_APPS.
5)  Pada direktori main, saya membuat direktori main, saya membuat direktori templates yang berisi file main.html yang akan ditampilkan pada saat menjalankan proyek.
6)  Tentunya, file tersebut memerlukan model sehingga saya menambahkan class Product pada models.py di direktori main.
7)  Selain itu, dijalankan perintah membuat migrasi model dan menerapkan migrasi ke dalam basis data lokal.
8)  Sedangkan, data yang akan ditampilkan pada _template_ dibuat dalam fungsi show_main pada file views.py yang terdapat pada direktori main.
9)  Saya juga mengonfigurasi _routing_ URL aplikasi main dan _routing_ URL proyek.
10) Sebelum menyimpan perubahan pada repository, saya juga membuat unit test pada file test.py di direktori main dan menjalankannya.
11) Perubahan yang sudah saya lakukan sebelumnya saya simpan di repository library di github. Berikutnya saya meng-_upload_ proyek saya di adaptable.io.
12) Setelahnya, saya juga membuat perubahan-perubahan untuk menyelesaikan bagian-bagian tugas yang belum terselesaikan. Tentunya, saya selalu melakukan _add_, _commit_, dan _push_ sehingga repositori library selalu menampilkan yang terbaru.

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
Jawaban:
Bagan:

Penjelasan bagan yaitu sebagai berikut.
1) Saat suatu komputer mengakses sebuah aplikasi atau situs web, akan dikirimkan _request_ ke internet.
2) _Request_ tersebut diterima oleh urls.py.
3) Kemudian URL akan di-_routing_ dari urls.py di proyek ke urls.py aplikasi yang dituju. Lalu routing ke views.py dari aplikasi tersebut.
4) Data yang akan ditampilkan memerlukan model yang disediakan oleh models.py sehingga views.py akan mengakses models.py untuk menyimpan data dari views.py pada models.py. Selain itu, data yang akan diakses models.py bisa saja disimpan dalam _database_.
5) Aplikasi akan me-_render_ data yang ditampilkan dalam bentuk main.html yang merupakan template kode.
6) Kemudian, bentuk halaman web yang sudah dijalankan akan dikembalikan ke internet yang kemudian dapat diakses komputer pengguna.

**Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Jawaban:
Kita menggunakan virtual environment karena membantu untuk tetap memisahkan _dependencies_ masing-masing proyek apabila kita membuat proyek dengan versi Python yang berbeda. Hal ini disebabkan karena masing-masing versi Python memiliki versi paket yang berbeda.
Ya, kita tetap dapat membuat aplikasi web tanpa virtual environment apabila versi python yang digunakan sama. Jika masing-masing proyek yang berkaitan menggunakan versi Python yang berbeda dapat menimbulkan masalah karena _dependencies_ yang dimiliki berbeda.

**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
Jawaban:
Definisi:
- MVC (Model-View-Controller) adalah sebuah desain pola arsitektur yang memisahkan sebuah aplikasi menjadi komponen model, view, dan controller.
- MVT (Model-View-Template) adalah sebuah desain pola arsitektur untuk membuat sebuah aplikasi web denagn memisahkan aplikasi menjadi mode, view, dan template.
- MVVM (Model-View-ViewModel) adalah sebuah desain pola arsitektur yang mengatasi kekurangan MVP (Model-View-Presenter) dan MVC dengan memisahkan antara logika yang akan ditampilkan atau UI (User Interface) dengan inti dari logika bisnis aplikasi.
Perbedaan:
MVC:
- MVC memiliki _controller_ yang menjalankan model dan _view_.
- _View_ memberitahukan pengguna mengenai data yang akan ditampilkan.
- _View_ dan model sangat berkaitan.
- Pada MVC, kita harus menulis seluruh _control_ dengan kode yang spesifik.
- Sulit untuk dimodifikasi.
- Cocok untuk mengembangkan sebuah proyek skala besar.
- Tidak melibatkan pemetaan URL.
- Unit testing terbatas.
- Penerapan pada ASP.NET MVC dan Spring MVC.
MVT:
- _View_ digunakan untuk menerima HTTP _request_ dan mengembalikan HTTP _response_.
- _Template_ digunakan untuk menampilkan data pengguna.
- _View_ dan model tidak terlalu berkaitan.
- _Controller_ diatur oleh _framework_.
- Modifikasi mudah.
- Cocok untuk proyek skala kecil dan beasr.
- Melibatkan pemetaan URL.
- Mudah menggunakan _unit testing_.
- Penerapan pada Django.
MVVM:
- Lebih _event-driven_ karena memisahkan _business logic_ dan _View_.
- Banyak _View_ dapat dipetakan dengan sebuah _ViewModel_ sehingga _View_ memiliki referensi ke _ViewModel_.
- Mudah untuk dimodifikasi.
- Tidak cocok untuk proyek skala kecil.
- _Unit testability_ pada arsitektur ini merupakan yang tertinggi.
- Penerapan pada Xamarin.
