#zad1

# A=[1-x for x in range(1,10)]
# print(A)
# B=[4**i for i in range(0,7)]
# print(B)
# C = [x for x in B if x%2==0]
# print(C)

#zad2
import random

# randomlist = []
# for i in range(0,10):
#     n = random.randint(1,100)
#     randomlist.append(n)
#
# parzystalista= [x for x in randomlist if x%2==0]
#
# print(randomlist)
# print(parzystalista)

#Zad3
#
# produkty = {"Chleb":"szt","Maka":"kg","Herbata":"saszetki"}
# listaprodktow = {value: key for key, value in produkty.items()}
#
# print(listaprodktow)
#zad4
# def trojkat(a,b,c):
#     if a**2+b**2 == c**2:
#         print("Trojkat jest prostkatny")
#     else:
#         print("Trojkat nie jest prostokątny")
#
# trojkat(3,4,5)

#zad5

# def trapez(a=2,b=4,h=5):
#     print((a+b)/2*h)
#
# trapez()

#zad6
# def ciag(a1= 1, b= 4,ile= 10):
#     print((a1*(1-(b**ile)))/(1-b))
# ciag()

#zad7
# def ciag(* argumenty):
#     print((argumenty[0]*(1-(argumenty[1]**argumenty[2])))/(1-argumenty[1]))
# ciag(1,4,10)

#zad8
def suma(** rzeczy):
    sumaw =0
    for i in rzeczy:
       sumaw +=rzeczy[i]
    return (sumaw)

print(suma(czekolad=1, chleb=2,maslo=3))