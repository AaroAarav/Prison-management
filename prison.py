import pickle



def NewFile():
  try:
   with open("PRISON.DAT","wb") as F:
     while True:
       ID=int(input("ID:"))
       Name=input("Name:")
       Crime=input("Crime Comitted")
       Duration=input("Duration")
       pickle.dump([ID,Name,Crime,Duration],F)
       Q=input("More Names(Y/N)?")
       if Q =='N':
         break
  except:
   print("File not found")

def DelName():
  L=[]
  with open("PRISON.DAT","rb+") as F:
    A=int(input('Enter ID no. to delete record: '))
    while True:
      try:
        IT=pickle.load(F)
        if A!=IT[0]:
          print(IT[0])
          L.append(IT)
      except:
        break
    F.seek(0)
    pickle.dump(L,F)

def AddNames():
  with open("PRISON.DAT","ab") as F:
    while True:
      ID=int(input("ID:"))
      Name=input("Name:")
      Crime=input("Crime Comitted")
      Duration=input("Duration")
      pickle.dump([ID,Name,Crime,Duration],F)
      Q=input("More Names(Y/N)?")
      if Q == 'N':
        break

def ViewNames():
  try:
    with open("PRISON.DAT","rb") as F:
      while True:
        try:
          IT=pickle.load(F)
          print(IT)
        except:
          break
  except FileNotFoundError:
    print("No File!")



def SearchName():
  try:
    with open("PRISON.DAT","rb") as F:
      IN=input("Name to Search:");Found=0
      while True:
        try:
          IT=pickle.load(F)
          if IT[1]==IN:
            print(IT);Found=1;break
        except:
          break
      if not Found:
        print("Name not found!")
  except FileNotFoundError:
    print("No File!")

def Change():
  try:
    with open("PRISON.DAT","rb+") as F:
      R=pickle.load(F)
      for L in R:
        print(L)
        C=input("Modify(Y/N)?")
        if C in ('Y','y'):
          a=int(input("New ID"))
          b=input("New Name:")
          c=input("New Crime Commited")
          d=input("New Duration")
          L[0]=a
          L[1]=b
          L[2]=c
          L[3]=d
      F.seek(0)
      pickle.dump(R,F)
  except FileNotFoundError:
    print("No File!")

C=['CSHM']
D=['CSHM@123']

while True:
   print("""Welcome user!
        1) Signup
        2) Login
        3) Forgot Password
        4) Exit
        Enter your choice:
        """)
   O=input()
   if O=='1':
     c=input('Enter New Username: ')
     d=input('Enter New Password: ')
     C.append(c)
     D.append(d)
   elif O=='3':
     a=input('Enter your Username: ')
     if a in C:
       b=C.index(a)
     print("Your old password is: ", D[b])
   elif O=='2':
     A=input('Enter Admin Username: ')
     B=input('Enter Admin Password: ')
     if A in C:
       if B in D:
        while True:
          Q=input("N:NewFile\V:View\A:Add\D:Delete\S:Search\C:Change:")


           # NewFile AddPrisoner SearchName ViewName
          if Q in 'nN':
           NewFile()
          elif Q in 'vV':
           ViewNames()
          elif Q in 'aA':
           AddNames()
          elif Q in 'sS':
           SearchName()
          elif Q in 'cC':
           Change()
          elif Q in 'dD':
           DelName()
          else:
           break
   elif O=='4':
     break


