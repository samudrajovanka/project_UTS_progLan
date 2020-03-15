'''
Project Program Lanjut

Jovanka Samudra
Marshall Anugrah Najmi
Daffy Ramzi
'''

# mengambil library os
import os

def popLeft(arr):
    val=arr[0]

    # memajukan data array ke depan
    for i in range (len(arr)-1):
        arr[i]=arr[i+1]
         
    # menghapus elemen array terakhir
    arr[-1:] = []
    return val

def getMid(arrs, lengthArr, data = [], queue = []):
    if len(data) == lengthArr:
        return data
    else:
        # memasukan ke dalam list queue jika ada 2 data
        if len(arrs) == 2:
            for arr in arrs:
                # memasukan arr jika panjangnya tidak 0
                if len(arr) != 0:
                    queue.append(arr)
        # memasukan ke dalam list queue jika ada satu data
        else:
            queue.append(arrs)

        # mengeluarkan list terdepatan pada list queue
        valPop = popLeft(queue)
        # mencari titik tengah dari valPop
        indMid = (len(valPop))//2
        # memasukan nilai tengah pada valPop ke list data
        data.append(valPop[indMid])
        # membagi dua list menjadi left dan right
        left = valPop[:indMid]
        right = valPop[indMid+1:]
        arrs = [left, right]

        # merekursif fungsi getMid
        return getMid(arrs, lengthArr)

# membuat main
if __name__ == "__main__":
    # membuat fungsi untuk clear screen (anonymous function)
    cls_scr = lambda: os.system("cls")

    # inisislisasi variable
    f_arr = []
    is_continue = True

    while is_continue :
        limit = int(input("Masukan limit array = "))
        if limit < 21:
            print("Limit yang anda masukan kurang dari 21\n")
        else: 
            is_continue = False
            for i in range(limit):
                f_arr.append(int(input(f"Angka elemen ke-{i+1}: ")))

            cls_scr()
            print("Data asli =", f_arr)
            length = len(f_arr) 
            results = getMid(f_arr, length)
            print("Data hasil =", results)