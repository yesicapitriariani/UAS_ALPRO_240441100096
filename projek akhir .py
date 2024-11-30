print("selamat datang di program untuk menurunkan berat badan")

kalori_per_olahraga = {
    "sepeda": 400,
    "push up": 300,
    "lari": 400,
    "lompat tali": 300,
    "yoga": 400,
    "sit up": 300,
}

def hitung_penurunan_bb(bb_awal, olahraga_harian):
    total_kalori = 0
    for olahraga in olahraga_harian:
        total_kalori += kalori_per_olahraga[olahraga]
    penurunan_bb = total_kalori / 7700  
    bb_akhir = bb_awal - penurunan_bb
    
    return bb_akhir

def create_olahraga():
    olahraga_baru = input("masukkan nama olahraga baru: ")
    kalori = int(input(f"masukkan kalori yang dibakar untuk {olahraga_baru}: "))
    kalori_per_olahraga[olahraga_baru] = kalori
    print(f"olahraga {olahraga_baru} telah ditambahkan dengan kalori {kalori}.")

def read_olahraga():
    print("daftar olahraga yang ada:")
    for olahraga, kalori in kalori_per_olahraga.items():
        print(f"{olahraga}: {kalori} kalori")

def update_olahraga():
    olahraga = input("Masukkan nama olahraga yang ingin diupdate: ")
    if olahraga in kalori_per_olahraga:
        kalori = int(input(f"Masukkan kalori baru untuk {olahraga}: "))
        kalori_per_olahraga[olahraga] = kalori
        print(f"Olahraga {olahraga} telah diperbarui menjadi {kalori} kalori.")
    else:
        print("Olahraga tidak ditemukan.")

def delete_olahraga():
    olahraga = input("Masukkan nama olahraga yang ingin dihapus: ")
    if olahraga in kalori_per_olahraga:
        del kalori_per_olahraga[olahraga]
        print(f"olahraga {olahraga} telah dihapus.")
    else:
        print("olahraga tidak ditemukan.")

def main():
    while True:
        print("menu")
        print("1. tambah olahraga")
        print("2. tampilkan olahraga")
        print("3. update olahraga")
        print("4. hapus olahraga")
        print("5. mulai program penurunan berat badan")
        print("6. keluar")
        
        pilihan = input("pilih menu (1-6): ")
        
        if pilihan == '1':
            create_olahraga()
        elif pilihan == '2':
            read_olahraga()
        elif pilihan == '3':
            update_olahraga()
        elif pilihan == '4':
            delete_olahraga()
        elif pilihan == '5':
            bb_awal = float(input("masukkan berat badan awal kamu (kg): "))
            target_bb = float(input("masukkan target berat badan yang kamu inginkan (kg): "))
            
            berat_yang_harus_turun = bb_awal - target_bb
            print(f"anda ingin menurunkan berat badan sebanyak {berat_yang_harus_turun:.2f} kg.")
            
            berat_harian = [bb_awal]

            for hari in range(1, 30): 
                print(f"Hari ke-{hari}:")
                olahraga_harian = []
                
                print("silahkan pilih olahraga yang ingin kamu lakukan:")
                for olahraga in kalori_per_olahraga:  
                    print(f"- {olahraga}")
                
                while True:
                    if len(olahraga_harian) < 2:
                        pilihan = input(f"masukkan jenis olahraga yang kamu lakukan (atau ketik 'tidak olahraga' jika kamu tidak melakukan berolahraga): ")
                        
                        if pilihan == 'tidak olahraga':
                            print("anda memilih untuk tidak berolahraga hari ini. Hari ini dilewati.")
                            berat_harian.append(berat_harian[-1])  
                            break  
                        
                        if pilihan in kalori_per_olahraga:
                            if pilihan not in olahraga_harian:  
                                olahraga_harian.append(pilihan) 
                            else:
                                print("anda sudah memasukkan olahraga ini. Silakan pilih olahraga lain.")
                        else:
                            print("olahraga tidak ditemukan. Silakan coba lagi.")
                    else:
                        break 

                if len(olahraga_harian) == 2:  
                    bb_akhir = hitung_penurunan_bb(berat_harian[-1], olahraga_harian)
                    berat_harian += [bb_akhir] 
                    print(f"berat badan saat ini setelah hari ke-{hari}: {bb_akhir:.2f} kg")
                    
                    if bb_akhir <= target_bb:
                        print("selamat! Kamu telah mencapai target berat badan yang kamu inginkan.")
                        break
                else:
                    print(f"tidak ada olahraga yang dilakukan hari ini. Berat badan tetap: {berat_harian[-1]:.2f} kg")


            print("List berat badan anda setiap hari:")
            for i in range(len(berat_harian)): 
                if berat_harian[i-1] == berat_harian[i]:
                    print(f"Hari ke-{i}: Anda tidak olahraga")
                else:
                    print(f"Hari ke-{i}: {berat_harian[i]:.2f} kg")

        elif pilihan == '6':
            print("terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("pilihan tidak valid. Silakan pilih menu yang benar.")

main()