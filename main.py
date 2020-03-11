# # def divide(n, side):
# #     if n != 0:
# #         n = n//2
# #         if side == 'L':
# #             print(side)
# #             side = 'R'
# #             divide(n, side)
# #         else:
# #             print(side)
# #             side = 'L'
# #             divide(n, side)
# #     else:
# #         print(side)

# # divide(10, 'L')

# # def divide(arr, temp_Arr, side = 'L', ind = 0):
# #     if len(arr) != 0:
# #         temp_Arr.append([])
# #         mid_Ind = (len(arr)-1)//2
# #         temp_Arr[-1] = arr[mid_Ind]
# #         if side == 'L':
# #             print(side)
# #             divide(arr[:mid_Ind], temp_Arr, side = 'R', ind = mid_Ind)
# #         else:
# #             print(side)
# #             divide(arr[ind+1:], temp_Arr, side = 'L')
# #     else:
# #         print(temp_Arr)

# # arr = [1,2,3,4,5,6,7,8,9,10]
# # temp_Arr = []
# # divide(arr, temp_Arr)

# def divide(arr, temp_arr, temp_left = [], temp_right = [], side = 'R'):
#     if len(arr) != 0:
#         ind_mid = (len(arr)-1)//2
#         print(ind_mid, side)
        
#         if side =='R':
#             temp_right.append([])
#             temp_right[-1] = arr[ind_mid]
#             print('val = ', temp_right)
#         else:
#             temp_left.append([])
#             temp_left[-1] = arr[ind_mid]
#             print('val = ',temp_left)

#         divide(arr[:ind_mid], temp_arr, temp_left, temp_right, side = 'L')
#         divide(arr[ind_mid+1:], temp_arr, temp_left, temp_right, side = 'R')
#     else:
#         temp_arr.append([])
#         print('panjang temparr = ', len(temp_arr))
        
#         print('val right = ', temp_right)
#         print('val left = ',temp_left)
#         i = 0
#         j = 0
#         for i in range(len(temp_arr)):
#             print(i)
#             if i % 2 == 0:
#                 temp_arr[i] = temp_right[i]
#                 i += 1
#             else:
#                 temp_arr[i] = temp_left[j]
#                 j += 1
#             print('val temp = ',temp_arr)

#         # print(temp_arr)

# arr = [1,2,3,4,5,6,7,8,9,10]
# temp_arr = []
# divide(arr, temp_arr)

from collections import deque

# def mid(*args, temp_arr, temp = [], data = deque()):
#     if len(temp_arr) != 10:
#         print('isi data sebelum = ', data)
#         for i in args:
#             data.append(i)
#             print(data)

#         val_pop = data.popleft()
#         print('isi data setelah pop = ', data)
#         print('isi val_pop = ',val_pop)
#         ind_mid = (len(val_pop))//2
#         print('isi ind_mid = ',ind_mid)
#         temp_arr.append(val_pop[ind_mid])
#         print('isi temp_arr = ',temp_arr)
#         # print(val_pop[ind_mid])
#         print('sisi kiri = ', val_pop[:ind_mid])
#         print('sisi kanan = ', val_pop[ind_mid+1:], '\n\n')
#         if ind_mid != 1 and ind_mid != 0:
#             print('masuk if')
#             mid(val_pop[:ind_mid], val_pop[ind_mid+1:], temp_arr = temp_arr, data = data)
#         elif ind_mid == 0:
#             print('masuk 0')
#             mid(temp_arr = temp_arr, data = data)
#         else:
#             mid(val_pop[:ind_mid], temp_arr = temp_arr, data = data)
#         # mid(val_pop[ind_mid+1:], temp_arr = temp_arr)
#     else:
#         print(temp_arr)

# a = [1,2,3,4,5,6,7,8,9,10]
# b = []
# mid(a, temp_arr = b)

def getMid(*args, temp = [], data = deque()):
    if len(temp) != 10:
        for i in args:
            data.append(i)

        val_pop = data.popleft()
        ind_mid = (len(val_pop))//2
        temp.append(val_pop[ind_mid])

        if ind_mid == 0:
            getMid(data = data)
        elif ind_mid == 1:
            getMid(val_pop[:ind_mid], data = data)
        else:
            getMid(val_pop[:ind_mid], val_pop[ind_mid+1:], data = data)
    else:
        print(temp)

a = [1,2,3,4,5,6,7,8,9,10]

# b = getMid(a)
getMid(a)
# print(b)


