file = open ("db-inventory.txt","a")
while True:
    tidak = input ("Input data inventory baru ? (ya/tidak)")
    if tidak == 'tidak' or tidak == 'Tidak':
        file = open ("db-inventory.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        break
    if tidak == 'ya' or tidak == 'Ya':
        print(".............................")
        x = input ("Masukan Nama Perangkat : ")
        y = input ("Masukan Lokasi : ")
        file.write("Nama Perangkat : " +x + ", Lokasi : " + y +"\n")
        print(".............................")
file.close()