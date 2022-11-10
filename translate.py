from csv import *
import datetime
import time
import tracemalloc

#To measure the memory usage
tracemalloc.start()

#To measure the time taken for the process
begin = datetime.datetime.now()

#find_Words file reading
file1=open("find_words.txt","r")
m=file1.read()

#t8.shakespeare file reading
file2=open("t8.shakespeare.txt","r")
n=file2.read()

#dict csv file reading
f=open("french_dictionary.csv","r")
o=reader(f)
li=[]
num=0

#This loop ussing to convert csv into the list format
for k in o:
   li.append(k)
   
#This method used to convert list to dictionary
dic=dict(li)
#This method split words and shakespeare file words into seperate
a=m.split("\n")
b=n.split(" ")

#This innner forloops used to find same word in find_words file and t8.shakespeare file and translate into french
cont=[]
for i in a:
    num2=0
    for j in b:
        if ( i == j ):
           
            val=dic.get(i)
            if (i == val):
                continue
            else:
                ind=b.index(j)
                num += 1
                num2 += 1
                b[ind]=val
                        
    if (num2 > 0):
        val=dic.get(i)
        li=[i,val,num2]
        cont.append(li)

st=" ".join(b)
file1=open("t8.shakespeare.txt","w")
file1.write(st)
file1.close()

#creating a csv file to count the frequency
csv=open("Frequency.csv","w")
head=["English words","French words","Frequency"]
wr=writer(csv)
wr.writerow(head)
wr.writerows(cont)
csv.close()
print("file saved...")

#The end process of the timer       
end=datetime.datetime.now()
print(tracemalloc.get_traced_memory())
print(f"The number of time taken {end-begin} seconds ") 
print("num",num)          
tracemalloc.stop()