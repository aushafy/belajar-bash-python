#!/usr/bin/python3.9

import os

gambar = ['https://cdns.klimg.com/resized/476x/selebriti/Chelsea_Islan/p/chelsea-islan-1022.jpg','https://dokterhewan.co.id/po-content/uploads/kucing-bengal-marble.jpg','https://gizmostory.com/wp-content/uploads/2021/07/Alice-In-Borderland-Season-2.jpg']

# Melakukan pengulangan sebanyak panjang dari array gambar. dalam kasus ini adalah 3
for i in range(len(gambar)):
  # menjalankan perintah wget dengan meletakkan hasil download ke direktori /tmp/gambar
  # format penamaan filenya akan menjadi /tmp/gambar1 /tmp/gambar2 /tmp/gambar3
  os.system("wget -O /tmp/gambar" + str(i) + ".jpg" + " " + str(gambar[i]))
  
# menampilkan hasil download ke layar terminal
os.system("ls /tmp/ | grep gambar")