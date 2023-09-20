Khansa Mahira

2206819413

PBP D


**Tugas 2**

Web: https://library-deploy.adaptable.app


**Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).**

Jawaban:
1)  Saat membuat aplikasi Django, saya memulai dari membuat direktori bernama library yang saya inisialisasikan dengan github.
2)  Berikutnya saya membuat repositori bernama library di github untuk menyimpan direktori aplikasi secara virtual.
3)  Pada direktori library di komputer saya, saya membuat dan mengaktifkan _environment_ Django dengan memanfaatkan isi dari requirements.txt sehingga memudahkan saya tanpa perlu menyusun kode aplikasi dari awal.
4)  Selanjutnya, saya membuat aplikasi main. Setelah dibuat direktori main, maka pada settings.py dalam direktori library, saya menambahkan main pada list INSTALLED_APPS.
5)  Pada direktori main, saya membuat direktori templates yang berisi file main.html yang akan ditampilkan pada saat menjalankan proyek.
6)  Tentunya, file tersebut memerlukan model sehingga saya menambahkan class Product pada models.py di direktori main.
7)  Selain itu, dijalankan perintah membuat migrasi model dan menerapkan migrasi ke dalam basis data lokal.
8)  Sedangkan, data yang akan ditampilkan pada _template_ dibuat dalam fungsi show_main pada file views.py yang terdapat pada direktori main.
9)  Saya juga mengonfigurasi _routing_ URL aplikasi main dan _routing_ URL proyek.
10) Sebelum menyimpan perubahan pada repositori, saya juga membuat unit test pada file test.py di direktori main dan menjalankannya.
11) Perubahan yang sudah saya lakukan sebelumnya saya simpan di repositori library di github. Berikutnya saya meng-_upload_ proyek saya di adaptable.io.
12) Setelahnya, saya juga membuat perubahan-perubahan untuk menyelesaikan bagian-bagian tugas yang belum terselesaikan. Tentunya, saya selalu melakukan _add_, _commit_, dan _push_ sehingga repositori library selalu menampilkan yang terbaru.


**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

Jawaban:

Bagan:

![KhansaMahira_Tugas2](https://github.com/KhansaMahira/library/assets/110018127/aba947c3-869a-490f-b423-580e87b486a4)

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
- MVT (Model-View-Template) adalah sebuah desain pola arsitektur untuk membuat sebuah aplikasi web dengan memisahkan aplikasi menjadi mode, view, dan template.
- MVVM (Model-View-ViewModel) adalah sebuah desain pola arsitektur yang mengatasi kekurangan MVP (Model-View-Presenter) dan MVC dengan memisahkan antara logika yang akan ditampilkan atau UI (User Interface) dengan logika bisnis aplikasi.

Perbedaan:

MVC:
- MVC memiliki _controller_ yang menjalankan model dan _view_.
- _View_ memberitahukan pengguna mengenai data yang akan ditampilkan.
- _View_ dan model sangat berkaitan.
- Pada MVC, kita harus menulis seluruh _control_ dengan kode yang spesifik.
- Sulit untuk dimodifikasi.
- Sesuai untuk mengembangkan sebuah proyek skala besar.
- Tidak melibatkan pemetaan URL.
- _Unit testing_ terbatas.
- Penerapan pada ASP.NET MVC dan Spring MVC.

MVT:
- _View_ digunakan untuk menerima HTTP _request_ dan mengembalikan HTTP _response_.
- _Template_ digunakan untuk menampilkan data pengguna.
- _View_ dan model tidak terlalu berkaitan.
- _Controller_ diatur oleh _framework_.
- Modifikasi mudah.
- Sesuai untuk proyek skala kecil dan beasr.
- Melibatkan pemetaan URL.
- Mudah menggunakan _unit testing_.
- Penerapan pada Django.

MVVM:
- Memisahkan _business logic_ dan _View_ sehingga lebih _event-driven_.
- Banyak _View_ dapat dipetakan dengan sebuah _ViewModel_ sehingga _View_ memiliki referensi ke _ViewModel_.
- Mudah untuk dimodifikasi.
- Tidak sesuai untuk proyek skala kecil.
- _Unit testability_ pada arsitektur ini merupakan yang tertinggi.
- Penerapan pada Xamarin.


**Tugas 3**


**Apa perbedaan antara form POST dan form GET dalam Django?**

Jawaban:

Form POST:
- Proses pada form Post dimulai dari data form digabungkan, berikutnya di-_encode_ untuk transmisi lalu dikirim ke server. Terakhir, respons akan diterima kembali.
- Sesuai dengan prosesnya, POST digunakan untuk data yang berhubungan dengan keamanan seperti _password_.
- POST digunakan untuk _request_ yang dapat merubah keadaan sistem.

Form GET:
- Proses pada form GET dimulai dari menggabungkan data yang dikirimkan ke dalam string untuk membuat URL sehingga URL berisi alamat tujuan pengiriman data, beserta _key_ dan _value_-nya.
- GET digunakan pada _request_ yang tidak mempengaruhi keadaan sistem.
- GET digunakan untuk sebuah halaman pencarian karena URL dari GET _request_ mudah untuk ditandai, dibagikan, atau dikirim ulang.


**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

Jawaban:

XML:

XML digunakan untuk menyimpan atau mengirim data. Data XML bersifat _self-describing_ sehingga dapat diproses dan ditampilkan dengan cara yang tidak terbatas. XML menyimpan data menggunakan _tag_ yang dapat didefinisikan oleh pengguna sehingga dapat disesuaikan dengan kebutuhan.

JSON:

Format data yang digunakan JSON yaitu _human-readable text_ yang terdiri dari atribut berupa _key_ dan _value_. Setiap pasangan _key_ dan _value_ pada JSON selalu diawali dan diakhiri dengan kurung kurawal. Data tersebut digunakan untuk menyimpan dan mengirimkan objek data yang terstruktur.

HTML:

HTML digunakan untuk memformat dan menampilkan data. Data yang disimpan dalam HTML pada _element_ dapat menggunakan _attribute_ di dalam _tag_sehingga lebih fleksibel.


**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

Jawaban:

JSON memiliki beberapa keunggulan yaitu sebagai berikut.
- Kesederhanaan karena strukturnya lebih simpel.
- Keterbacaan karena JSON memiliki format _text-based_ dalam bentuk pasangan _key_ dan _value_.
- Bersifat _lightwieght_ sehingga lebih efisien.
- _Performance_ JSON lebih cepat dibandingkan XML.
- JSON mendukung tipe data seperti null, string, boolean, numeric, object, dan array.
- Bersifat kompatibilitas dan interoperabilitas sehingga dapat digunakan pada berbagai macam _framework_, bahasa pemrograman, dan platform.


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Jawaban:

[ini jawaban]


 **_Screenshot_ dari hasil akses URL pada Postman**

HTML:


XML:


JSON:


XML _by ID_:


JSON _by ID_:
