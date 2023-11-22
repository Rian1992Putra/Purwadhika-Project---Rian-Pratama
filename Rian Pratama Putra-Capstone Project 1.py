
# CAPSTONE PROJECT 1 MODUL 1 - Rian Pratama Putra



import operator

# Data collection berupa dictionary didalam list
daftarBarang = [
    {'nama':'pulpen'     ,'stok':5, 'harga':3000},
    {'nama':'penghapus'  ,'stok':6, 'harga':4000},
    {'nama':'penggaris'  ,'stok':2, 'harga':5000},
    {'nama':'pensil'     ,'stok':3, 'harga':2000},
    {'nama':'spidol'     ,'stok':6, 'harga':6000},
    ]

# Function untuk menampilkan Menu Utama
def menuUtama():
    print('='*60)
    print('''Selamat datang di Toko Alat Tulis Rian\n
    Menu Utama :
    1. Menampilkan dan mencari barang
    2. Menambah jenis barang
    3. Mengubah stok atau harga barang
    4. Menghapus jenis barang
    5. Mengurutkan data
    6. Keluar aplikasi''')
    print('='*60)

# Function untuk menampilkan menu 'Menampilkan dan mencari barang'
def menu1():
    # Menampilkan daftar barang
    print('='*60)
    print('\t\t DAFTAR BARANG')
    print('Index|Nama Barang    |Jumlah    |Harga Satuan')
    for barang1 in range (len(daftarBarang)) :
        print('{:<5}|{:<15}|{:<10}|{}'.format(barang1, daftarBarang[barang1]['nama'],daftarBarang[barang1]['stok'],daftarBarang[barang1]['harga']))
    print('='*60)
    print('>> Mencari barang <<\n')
    # Pengecekan ketersediaan barang pada data collection menggunakan 'userinput'
    inputSubMenu1 = str(input('Masukkan nama barang yang ingin di cek : ')).lower()
    for satuanBarang1 in daftarBarang:
        if satuanBarang1['nama'] == inputSubMenu1 :
            print(f'\nBarang dengan nama \'{inputSubMenu1}\' ditemukan')
            print('='*60)
            break
    else : 
        print(f'\nBarang dengan nama \'{inputSubMenu1}\' tidak ditemukan')

# Function untuk menampilkan menu 'Menambah jenis barang'
def menu2():
    print('='*60)
    print('>> Menambah jenis barang <<\n')
    # Menambah jenis barang pada data collection menggunakan 'userinput'
    inputJenisBarangTambah = input('Masukkan nama barang yang akan ditambah : ').lower()
    for satuanBarang2 in daftarBarang:
        if satuanBarang2['nama'] == inputJenisBarangTambah:
            print(f'\nBarang dengan nama \'{inputJenisBarangTambah}\' sudah ada, silahkan pilih menu \'Mengubah stok atau harga barang\' bila ingin menambahkan stok')
            print('='*60)
            break
    else :  
        try :       
            inputStokBarang = int(input('Silahkan masukkan jumlah barang : '))
            inputHargaBarang = int(input('Silahkan masukkan harga satuan barang : '))
            daftarBarang.append({'nama': inputJenisBarangTambah, 'stok': inputStokBarang, 'harga': inputHargaBarang})
            print(f'\nBarang dengan nama \'{inputJenisBarangTambah}\' berhasil ditambahkan\n')
            print('\t\t DAFTAR BARANG')
            print('Index|Nama Barang    |Jumlah    |Harga Satuan')
            for barang2 in range (len(daftarBarang)) :
                print('{:<5}|{:<15}|{:<10}|{}'.format(barang2, daftarBarang[barang2]['nama'],daftarBarang[barang2]['stok'],daftarBarang[barang2]['harga']))
            print('='*60)
        except ValueError:
            print('\nInput harus berupa angka')

# Function untuk menampilkan menu 'Mengubah stok atau harga barang'
def menu3():
    print('='*60)
    print('>> Mengubah stok atau harga barang <<\n')
    # Mengubah data barang pada data collection menggunakan 'userinput' untuk menentukan data apa yang ingin diubah
    inputSubMenu3 = input('Silahkan masukkan jenis data yang ingin diubah \'harga\' atau \'stok\' : ').lower()
    # Mengubah data harga barang satuan pada data collection menggunakan 'userinput'
    if inputSubMenu3 == 'harga' :
        inputNamaBarang = input('Masukkan nama barang yang ingin diubah harganya : ').lower()
        for satuanbarang3 in daftarBarang:
            if 'nama' in satuanbarang3:
                if satuanbarang3['nama'] == inputNamaBarang :
                    try :
                        inputUbahHarga = int(input ('Masukkan data harga barang satuan baru : '))
                        satuanbarang3['harga'] = inputUbahHarga
                        print(f'\nHarga barang \'{inputNamaBarang}\' berhasil diubah menjadi \'{inputUbahHarga}\' ')
                        print('\n\t\t DAFTAR BARANG')
                        print('Index|Nama Barang    |Jumlah    |Harga Satuan')
                        for item3 in range (len(daftarBarang)) :
                            print('{:<5}|{:<15}|{:<10}|{}'.format(item3, daftarBarang[item3]['nama'],daftarBarang[item3]['stok'],daftarBarang[item3]['harga']))
                        print('='*60)
                        break
                    except ValueError:
                        print('\nInput harus berupa angka')
                        break    
        else:
            print(f'\nInput yang anda masukkan salah karena tidak ada barang \'{inputNamaBarang}\' pada sistem')
    # Mengubah data stok barang pada data collection menggunakan 'userinput'       
    elif inputSubMenu3 == 'stok' :
        inputNamaBarang = input('Masukkan nama barang yang ingin diubah jumlah stoknya : ').lower()
        for satuanbarang3 in daftarBarang :       
            if 'nama' in satuanbarang3:
                if satuanbarang3['nama'] == inputNamaBarang:
                    try :
                        inputUbahStok = int(input ('Masukkan data jumlah stok baru : '))
                        satuanbarang3['stok'] = inputUbahStok
                        print(f'\nStok barang \'{inputNamaBarang}\' berhasil diubah menjadi \'{inputUbahStok}\' ')
                        print('\n\t\t DAFTAR BARANG')
                        print('Index|Nama Barang    |Jumlah    |Harga Satuan')
                        for item3 in range (len(daftarBarang)) :
                            print('{:<5}|{:<15}|{:<10}|{}'.format(item3, daftarBarang[item3]['nama'],daftarBarang[item3]['stok'],daftarBarang[item3]['harga']))
                        print('='*60)
                        break
                    except ValueError:
                        print('\nInput harus berupa angka') 
                        break
        else:
            print(f'\nInput yang anda masukkan salah karena tidak ada barang \'{inputNamaBarang}\' pada sistem')
    else :
            print ('\ninput yang anda masukkan bukan \'harga\' atau \'stok\' ')

# Function untuk menampilkan menu 'Menghapus jenis barang'
def menu4():
    print('='*60)
    print('>> Menghapus jenis barang <<\n')
    # Menghapus jenis barang pada data collection menggunakan 'userinput'
    inputJenisBarangHapus = input('Masukkan nama barang yang akan dihapus : ').lower()
    for satuanBarang4 in daftarBarang:
        if satuanBarang4['nama'] == inputJenisBarangHapus:
            daftarBarang.remove(satuanBarang4)
            print(f'\nBarang dengan nama \'{inputJenisBarangHapus}\' berhasil dihapus\n')
            print('\t\t DAFTAR BARANG')
            print('Index|Nama Barang    |Jumlah    |Harga Satuan')
            for barang4 in range (len(daftarBarang)) :
                print('{:<5}|{:<15}|{:<10}|{}'.format(barang4, daftarBarang[barang4]['nama'],daftarBarang[barang4]['stok'],daftarBarang[barang4]['harga']))
            print('='*60)
            break
    else :
            print(f'\nBarang dengan nama \'{inputJenisBarangHapus}\' tidak ditemukan')
            print('='*60)

# Function untuk menampilkan menu 'Mengurutkan data'
def menu5():
    print('='*60)
    print('>> Mengurutkan data <<\n')
    # Melakukan sorting/mengurutkan data barang pada data collection menggunakan 'userinput' dengan pilihan 'nama', 'stok' atau 'harga'
    inputDataSorting = input('Silahkan pilih data apa yang ingin diurutkan \'nama\', \'stok\' atau \'harga\' : ').lower()
    # Mengumpulkan semua 'key' pada dictionary daftarBarang
    keySubMenu5 = set()
    for barang5 in daftarBarang:
        keySubMenu5.update(barang5.keys())
    if inputDataSorting in keySubMenu5:
        daftarBarang.sort(key=operator.itemgetter(inputDataSorting))
        print(f'\nBerhasil mengurutkan data berdasarkan data {inputDataSorting} barang\n')
        print('Index|Nama Barang    |Jumlah    |Harga Satuan')
        for satuanBarang5 in range (len(daftarBarang)) :
            print('{:<5}|{:<15}|{:<10}|{}'.format(satuanBarang5, daftarBarang[satuanBarang5]['nama'],daftarBarang[satuanBarang5]['stok'],daftarBarang[satuanBarang5]['harga']))
    else:
        print("\nInput yang anda masukkan salah")

# Function untuk menampilkan menu 'Keluar aplikasi'
def menu6():
    print('\nAnda akan keluar dari program, terima kasih') 
    print('='*60) 

# Program start
while True :
    # Menampilkan menu utama dan memasukkan input berupa angka untuk memilih menu
    menuUtama()
    try :
        pilihanMenu = int(input("Silahkan pilih menu berapa : "))
        if pilihanMenu == 1 :
            menu1()
        elif pilihanMenu == 2 :
            menu2()
        elif pilihanMenu == 3 :
            menu3()
        elif pilihanMenu == 4 :
            menu4()  
        elif pilihanMenu == 5 :
            menu5()     
        elif pilihanMenu == 6 :
            menu6()
            break
    except ValueError:
        print('\nInput yang anda masukkan bukan angka, silahkan masukkan input angka')