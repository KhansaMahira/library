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
- Sesuai untuk proyek skala kecil dan besar.
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
1. Saya mengatur routing pada library/urls.py dengan mengubah path('main/', include('main.urls')) menjadi path('', include('main.urls')).
2. Saya membuat /templates/base.html sebagai template halaman web.
3. Saya menambahkan 'DIRS': [BASE_DIR / 'templates'] pada TEMPLATES di library/settings.py.
4. Saya menyesuaikan kode pada main/templates/main.html.
5. Saya membuat struktur form pada main/forms.py sehingga dapat menerima produk yang akan saya tambahkan pada web.
6. Pada main/views.py saya juga menyesuaikan dengan menambahkan beberapa import yang dapat membantu dalam membuat fungsi create_product, show_xml, show_json, show_xml_by_id, dan show_json_by_id serta menyesuaikan fungsi show_main. Fungsi show_xml untuk mengembalikan data dalam bentuk XML. Fungsi show_json untuk mengembalikan data dalam bentuk JSON. Fungsi show_xml_by_id untuk mengembalikan data dalam bentuk XML berdasarkan id product. Fungsi show_json_by_id untuk mengembalikan data dalam bentuk JSON berdasarkan id product.
7. Oleh karena itu, saya perlu menyesuaikan import pada main/urls.py.
8. Berikutnya, saya membuat file create_product.html di main/templates untuk form POST.
9. Saya juga menyesuaikan main/templates/main.html untuk menampilkan data dalam bentuk web.
10. Saat mengerjakan tugas ini, saya menerima beberapa eror sehingga saya kembali melakukan migrasi dengan memperbaiki variabel yang telah saya buat di tugas sebelumnya.
12. Saya menggunakan Postman untuk membuat request GET dengan url http://localhost:8000/ untuk menampilkan bentuk HTML dari web saya. Dengan url http://localhost:8000/xml untuk menampilkan bentuk XML data web saya. Dengan url http://localhost:8000/json untuk menampilkan bentuk JSON data web saya. Dengan url http://localhost:8000/xml/[id] untuk menampilkan bentuk xml data berdasarkan ID yang saya masukkan pada web saya. Dengan url http://localhost:8000/json/[id] untuk menampilkan bentuk json data berdasarkan ID yang saya masukkan pada web saya.
13. Untuk menyelesaikan soal bonus saya mencoba menampilkan jumlah buku yang telah ditambahkan dengan menggunakan for loop dari main.html menggunakan Liquid template language. Walaupun begitu, saya menemui banyak eror sehingga saya melakukan for loop dalam fungsi _sum_ yang disimpan pada total_amount pada main/views.py yang ditampilkan pada main.html


 **_Screenshot_ dari hasil akses URL pada Postman**

HTML:
![html1](https://github.com/KhansaMahira/library/assets/110018127/25655e16-78da-4cb2-827f-28cfacdbea50)
![html2](https://github.com/KhansaMahira/library/assets/110018127/bf9fb480-b59d-4535-a3b4-bd74856505bb)
![html3](https://github.com/KhansaMahira/library/assets/110018127/c60c6e59-8fd7-4f8e-9db8-d9dc2a062a0d)
![html4](https://github.com/KhansaMahira/library/assets/110018127/83e9486e-af73-4d09-bf14-2d272d091085)


XML:
![xml](https://github.com/KhansaMahira/library/assets/110018127/0405c8b0-4924-4073-93f4-22d710b3aca7)


JSON:
![json](https://github.com/KhansaMahira/library/assets/110018127/2fc89dc0-2237-448c-ba66-bada5cbbc697)


XML _by ID_:
![xmlbyid1](https://github.com/KhansaMahira/library/assets/110018127/9affc08e-54ae-4a44-811c-db09a5348356)
![xmlbyid2](https://github.com/KhansaMahira/library/assets/110018127/413752f0-479b-4e10-b771-59a0d921a1eb)


JSON _by ID_:
![jsonbyid1](https://github.com/KhansaMahira/library/assets/110018127/1c634edc-a183-4fe6-ac79-617c623d84dd)
![jsonbyid2](https://github.com/KhansaMahira/library/assets/110018127/8c398f1c-490a-4d34-982b-a7fc6f339541)


**Tugas 4**


**Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**

Jawaban:

Django UserCreationForm digunakan untuk membuat akun pengguna baru pada aplikasi web.

Kelebihan:

Django UserCreationForm memudahkan _developer_ dalam membuat register dan sign in form dengan memanfaatkan konsep model.

Kekurangan:

Django UserCreationForm tidak mendeteksi secara langsung mengenai _password_ yang dituliskan oleh pengguna apabila _password_ memenuhi persyaratan yang telah ditampilkan di halawamn web atau tidak sehingga pengguna dapat membuat _password_ sesuai keinginan tanpa memenuhi persyaratan yang disarankan.


**Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

Jawaban:

Autentikasi:

Autentikasi memverifikasi bahwa pengguna adalah diri mereka sendiri dari akun yang telah dibuat. Sistem autentikasi pengguna menangani akun pengguna, grup, izin, dan sesi pengguna berbasis _cookies_. Sistem autentikasi bawaan Django menyediakan kerangka kerja yaang kuat dan fleksibel untuk mengelola autentikasi pengguna. Sistem ini meliputi model pengguna untuk menyimpan informasi pengguna, serta tampilan dan formulis untuk menangani _registration_, _login_, dan manajemen _password_.

Otorisasi:

Otorisasi menentukan hal-hal boleh dilakukan dalam aplikasi oleh pengguna yang diautentikasi. Sistem otorisasi Django dibangun di atas sistem autentikasinya dan memungkinkan _developer_ untuk mengontrol akses ke berbagai bagian aplikasi dengan mudah. Django menyediakan set izin untuk model bawaannya seperti menambah, mengubah, menghapus, serta mengizinkan _developer_ untuk membuat izin khusus untuk model mereka sendiri.

Keduanya penting karena autentikasi berkatian dengan otorisasi. Dengan autentikasi kita dapat memverifikasi pengguna. Sedangkan, izin yang boleh dilakukan oleh pengguna tersebut terdapat pada otorisasi.

**Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?**

Jawaban:

_Cookies_ adalah data yang disimpan di browser pengguna yang dapat berisi berbagai informasi yang menghasilkan pengetahuan tentang aktivitas internet pengguna. Tujuan utama _cookies_ adalah untuk mengidentifikasi pengguna dan menyajikan halaman web yang disesuaikan dengan pengguna sehingga perpindahan setiap halaman web lebih mudah, serta menyimpan informasi login pengguna.

Django menyediakan dukungan penuh untuk sesi anonim. _Session framework_ menyimpan data di sisi server dan mengabstraksi pengiriman dan penerimaan _cookies_. _Cookies_ berisi ID sesi, bukan data itu sendiri.

**Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

Jawaban:

Umumnya _cookies_ aman dalam pengembangan web, tetapi beberapa bisa digunakan untuk melacak pengguna tanpa persetujuan pengguna oleh _cybercriminal_. Beberapa risiko potensial yang harus diwaspadai:
- Masalah keamanan karena pencurian _cookie_, gangguan, pemutaran ulang, serangan cross-site scripting (XSS), atau serangan cross-site request forgery (CSRF).
- _Cookies_ dapat digunakan untuk melacak jejak _online_ kegiatan pengguna dan membuat sebuah profil berdasarkan hal tersebut.
- _Cookies_ dapat menimbulkan risiko terhadap privasi pengguna dengan mengizinkan pihak ketiga seperi pengiklan, pemerintah, atau pengguna lain, melacak seluruh _path_ di Internet.

**Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).**

Jawaban:
1. Pada main/views.py, saya membuat fungsi register yang akan digunakan untuk membuat akun baru pengguna web saya. Oleh karena itu, pada direktori main/templates, saya membuat register.html. Saya juga menambahkan path register pada urlpatterns setelah melakukan import register pada main/urls.py.
2. Selain register, diperlukan form login sehingga pengguna dapat masuk menuju halaman library page utama. Oleh karena itu, saya membuat fungsi login_user pada main/views.py dan file login.html pada main/templates. Saya juga menambahkan path login_user pada urlpatterns setelah melakukan import login_user pada main/urls.py.
3. Untuk melengkapi login, saya juga membuat fungsi logout dengan membuat fungsi logout_user pada main/views.py sehingga saya hanya perlu merevisi main/templates/main.html untuk menyiapkan tombol logout. Saya juga menambahkan path logout_user pada urlpatterns setelah melakukan import logout_user pada main/urls.py.
4. Pada main/views.py saya mengimport login_required yang digunakan pada @login_required(login_url='/login') sebelum fungsi show_main sehingga halaman main hanya bisa diakses pengguna yang telah login.
5. Saya memanfaatkan _cookies_ untuk menampilkan data last_login pada halaman main dengan cara import HttpResponseRedirect, reverse, dan datetime pada main/views.py. Oleh karena itu, saya merevisi blok if user not None pada fungsi login_user termasuk set cookie pada response. Saya juga merevisi fungsi logout_user termasuk menambahkan delete cookie pada response. Untuk menampilkan data last_login pada halaman web, maka saya menambahkan kode last_login pada main/templates/main.html.
6. Karena web yang saya buat membutuhkan akun pengguna maka saya mengimport User pada main/models.py serta menambahkan user pada class Product. Oleh karena itu saya juga perlu merevisi fungsi create_product dan show_main pada main/views.py. Lalu saya melakukan migrasi.
7. Saya mencoba proyek dengan menjalankan proyek, membuat akun, login, menambahkan product, dan logout.
