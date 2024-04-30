#user1 = input()
#while True:
 #   user2 = input()
  #  if user1 [-1] !=user2[0]:
   #     print(user2)
    #    user1 = user2
#msg = input("Введите слово ")
#for i in msg:

    #print(ord(i),";",end ="")
#arr = []
#while True:

 #   user_inp = input("Введите рост:")
  #  if user_inp =="!":
   #     break
    #else:
     #   arr.append(user_inp)
#arr_right = []
#for item in arr:
#    if int(item) <=180 and int(item) >=160:
 #       arr_right.append(item)
#print(arr_right)
#print(min(arr_right))
#print(max(arr_right))
# while True:
# n = int(input("\n"))
# print("*"* n )
def find_sector(x,y):
    if x > 0 and y > 0:
        print("Сектор:1")
    elif x < 0 and y > 0:
        print("Сектор:2")
    elif x < 0 and y < 0:
        print("Сектор:3")
    elif x >0 and y <0:
        print("Сектор:4")

    find_sector(int(input("Введите X:")),int(input("Введите y:")))





