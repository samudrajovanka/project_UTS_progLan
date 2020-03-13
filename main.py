'''
Project Program Lanjut
Jovanka Samudra
Marshall Anugrah Najmi
Daffy Ramzi
'''

# mengambil library os
import os

# popLeft = mengeluarkan array indeks ke 0 dan menghapus elemen terakhir
def popLeft(arr):
    val=arr[0]

    # memajukan data array ke depan
    for i in range (0, len(arr)-1):
        arr[i]=arr[i+1]
         
    # menghapus elemen array terakhir
    arr[-1:] = []
    return val

def getMid(*arrs, lengthArr, data = [], queue = []):
    if len(data) == lengthArr:
        # print(data)
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

if __name__ == "__main__":
    # membuat fungsi untuk clear screen (anonymous function)
    cls_scr = lambda: os.system("cls")

    f_arr = []
    is_continue = True

    while is_continue :
        limit = int(input("Masukan limit angka yang ingin dimasukan = "))
        if limit < 21:
            print("Limit yang anda masukan kurang dari 21\n")
        else: 
            is_continue = False
            for i in range (0,limit):
                f_arr.append(int(input(f"Angka elemen ke-{i+1}: ")))

            cls_scr()
            print("Data asli =", f_arr)
            length = len(f_arr)
            results = getMid(f_arr, lengthArr=length)
            print("Data hasil = ", results)