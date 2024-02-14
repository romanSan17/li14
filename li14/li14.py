#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ").capitalize()
#    nimed.append(nimi)

  
#print("loetelu oli: ",nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ",nimed)

#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep="")
#print("Vimasena oli lisatud: ",nimi)

#uued_nimed=[]
#for nimi in nimed:
#    if nimi not in uued_nimed:
#        uued_nimed.append(nimi)
#print(uued_nimed)

#õpilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati', 'Mati']
#unikaalsed_õpilased=list(set(õpilased))
#print("unikaalne nimekiri:",unikaalsed_õpilased)


#vanus=[1,13,18,33,55]
#min_vanus = min(vanus)
#max_vanus = max(vanus)
#sum_vanus = sum(vanus)
#keskmine_vanus = sum_vanus / len(vanus)
#print("väikseim vanus:",min_vanus ,"suurim vanus:",max_vanus ,"vanus kokku:",sum_vanus ,"keskmine vanus:",keskmine_vanus )
#for i in range(5):
#    print (nimed[i], "on", vanus[i],"aastat vana")

#3
#from random import *
#arvud=[]
#N=int(input("Mitu rida joonistame? "))
#S=input("Sisesta sümbol: ")
#for p in range(N):
#    arvud.append(randint(1,100))
#for p in range(N):
#    print(arvud[p]*S)

#4
#indeksid=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    while True:
#        try:
#            indeks=int(input("Sisesta oma indeks: "))
#            #if<=10000indeks<=99999:
#            indeks_elemendide_arv=len(str(indeks))
#            if indeks_elemendide_arv==5:
#                print("5numbriline indeks")
#                break
#            else: 
#                print("On vaja 5numbriline arv(indeks)")
#        except:
#            print("Vale andmeyüüp!")
#    arv1=indeks//10000
#    print(arv1)
#    symbolid=list(str(indeks))
#    print(f"Sa elad piirkonnas {Indeksid[arv1-1]}")

#5
#list=[1,2,3,4,5,6,7,8]
#list.reverse()
#print(list)
    
#from random import *
#from string import *

#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#kogus=int(input("Mitu elemendi vahetame oma vahel "))
#if len(rida)//2>=kogus:
#    for i in range(kogus):
#        a=rida[i]
#        rida[i]=rida[len(rida)-i-1]
#        rida[len(rida)-1-i]=a
#print(rida)

#6
from random import *
number=[]
N=int(input("mitu numbrit on nimekirjas? "))
for o in range(N):
    number.append(randint(1,1000))
print(number)
max_num=max(number)
print("max numbri:", max_num)
kasutu=max_num / N
print("kasutu number:", kasutu)
number.insert(2,kasutu)
print(number)