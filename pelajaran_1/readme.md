## Pelajaran ke 1
**Tujuan**: Kenalan dengan library [Requests](https://requests.readthedocs.io/en/master/),  untuk berinteraksi dengan API

### Tugas ###
Lakukan interaksi dengan API secara programatis dengan code python pada API [Airport GAP](https://airportgap.dev-tester.com/docs):
- GET `/airports`
- GET `/airports/:id`
- POST `/airports/distance`

jangan lupa untuk eksplore sendiri dokumentasi API nya dan coba manual di Postman/curl

 ### Requests Librarry ###
 Dengan menggunakan bantuan library python kita bisa dengan mudah berinteraksi dengan API secara intuitif
 Untuk mengakses HTTP method GET, kita cukup menuliskan `requests.get(<url nya>)`
 Maka kita akan meneruma sebuah `response` object yang bisa kita olah lebih lanjut, secara umum kita bisa mengakses response seperti:
- `response.status_code`: http status code dari request tersebut
- `response.text`: response body dalam bentuk plain text
- `response.json()`: parses response body berupa json menjadi Python dictionary

### Referensi ###
- Dokumentasi Requests library: https://requests.readthedocs.io/en/master/
- Dokumentasi API https://airportgap.dev-tester.com/docs
- Contoh [jawaban](https://github.com/FachrulCH/belajar_api_test_python/blob/main/pelajaran_1/contoh_jawaban_1.py)
- Blog saya https://fachrul.id
- IG saya :p https://www.instagram.com/penguji.id/