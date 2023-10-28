#Function inputPengguna 
def inputPengguna(mesejInput):
  print(mesejInput)
  harga=float(input())
  return harga

#Procedure kiraPeratus
def kiraPeratus(h1,h2):
  peratus=((h2-h1)/h1)*100
  peratus=round(peratus,2)
  if peratus 0:
    print("Keuntungan ialah",peratus,"%")
  else:
    print("Kerugian ialah", abs(peratus),"%")

#Atur cara utama
h1=inputPengguna("Masukkan harga kos RM")
h2=inputPengguna("Masukkan harga jualan RM")

if h1 == h2:
  print("Tiada keuntungan")
else:
  kiraPeratus(h1,h2)
