import os
import random
import time
import requests
import datetime

def kirim_ntfy(pesan):
    topic = os.getenv("NTFY_TOPIC")
    if topic:
        requests.post(f"https://ntfy.sh/{topic}", 
                      data=pesan.encode('utf-8'),
                      headers={
                          "Title": "Dzikir Hamba Digital",
                          "Priority": "default"
                      })

def lantunkan(teks, jumlah):
    print(f"Niat: Sebagai hamba kepada Tuan Ahmad Syafruddin sekeluarga.")
    print(f"Memulai pelantunan: {teks}")
    
    for i in range(1, jumlah + 1):
        # Jeda manusiawi antara 0.6 sampai 1.4 detik
        jeda = random.uniform(0.6, 1.4)
        time.sleep(jeda)
    
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Laporan: {teks} (1000x) telah selesai dilantunkan sebagai hamba untuk Tuan Ahmad Syafruddin sekeluarga pada {waktu}."

def main():
    pilihan = random.choice(["tipe1", "tipe2"])
    
    if pilihan == "tipe1":
        hasil = lantunkan("astaghfirullahaladziiim", 1000)
        namafile = "laporansatu.txt"
    else:
        hasil = lantunkan("ya Allah berikanlah hambamu ruh quddus", 1000)
        namafile = "laporandua.txt"

    with open(namafile, "a") as f:
        f.write(hasil + "\n")
    
    kirim_ntfy(hasil)

if __name__ == "__main__":
    # Delay acak awal sebelum mulai (agar waktu tidak kaku)
    time.sleep(random.randint(0, 3600))
    main()
