'''
Project Program Lanjut

Jovanka Samudra
Marshall Anugrah Najmi
Daffy Ramzi
'''

# popLeft = mengeluarkan array indeks ke 0 dan menghapus elemen terakhir
def popLeft(arr):
    val=arr[0]

    # memajukan data array ke depan
    for i in range (0, len(arr)-1):
        arr[i]=arr[i+1]
         
    # menghapus elemen array terakhir
    arr[-1:] = []
    print('====isi setelah diapus =',arr)
    return val

def getMid(*arrs, lengthArr, data = [], queue = []):
    if len(data) == lengthArr:
        print(data)
        return data
    else:
        # memasukan per array ke dalam list queue (list untuk antrian pengambilan data) 
        for arr in arrs:
            queue.append(arr)

        # mengambil data dari fungsi popLeft
        val_pop = popLeft(queue)

        # mengambil indeks tengah-tengah dari array yang di pop
        ind_mid = (len(val_pop))//2

        # memasukan nilai tengah dari array yang di pop ke list data
        data.append(val_pop[ind_mid])

        if ind_mid == 0:
            # merekursif jika tidak ada data di kiri dan kanan
            getMid(lengthArr = lengthArr, queue = queue)
        elif ind_mid == 1:
            if len(val_pop) == 3:
                getMid(val_pop[:ind_mid], val_pop[ind_mid+1:], lengthArr = lengthArr, queue = queue)
            else:
            # merekursif jika hanya ada data di kiri
                getMid(val_pop[:ind_mid], lengthArr = lengthArr, queue = queue)
        else:
            # merekursif jika ada data di kiri dan kanan
            getMid(val_pop[:ind_mid], val_pop[ind_mid+1:], lengthArr = lengthArr, queue = queue)

a = [1,2,3,4,5,6,7,8]
length = len(a)
b = getMid(a, lengthArr=length)
print(b)