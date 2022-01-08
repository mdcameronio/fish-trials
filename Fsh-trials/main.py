#fish on
import random


from fmenu import head,menu,poles,netit,lnfhmen,drbt,neti
from jigit import jigging,jigging1
from fison import fishon
from relig import reeling,reeling1,reeling2,reeling3,reeling4
from dcast import wipit,wiped1,wiped2,wiped3,wiped4,wiped5


def usergreq():#save game
  head()
  while True:
    print("\n"*8,"           ------- Save Game  -------\n                      menu\n \n       a| Save Game       b| Load Saved Game\n       q| Main Menu","\n"*6)
    hsel = input("\nSelect from Menu\n")
    if hsel == "q":# quite to main
      head()#boat n hooks grafic
      menu()
      break
    elif hsel == "a":#save gear to a txt file
      with open("savegear.txt","w")as f:
        lstlg = len(yrgear)
        fied = yrgear[1:lstlg]
        for fi in fied:
          f.write(fi + "\n")
      with open("savewallet.txt","w")as f:
          f.write(str(wallet[-1]))
      print("\n"*20," -----> Your game has been saved.")
    elif hsel == "b":#load gear from txt
      yrgear.clear()
      yrgear.append("Tree branch")
      wallet.clear()
      with open("savegear.txt")as f:
        for line in f:
          line = line.strip()
          yrgear.append(line)
      with open("savewallet.txt")as f:
        for line in f:
          line = line.strip()
          wallet.append(int(line))
      print("\n"*20," -----> Game data loaded")
   


def pgear():#buy pole
  while True:
    head()
    poles()
    print("---> Your poles")
    for yr in yrgear:
        print("      ",yr)
    print("\nwallet balance $",wallet[-1])
    gsel = input("Enter selection\n")
    if gsel == "a" and wallet[-1] >= 100:
      cost =  wallet[-1] - 100
      wallet.append(cost)
      yrgear.append("Fenwick")
    elif gsel == "b" and wallet[-1] >= 90:
      cost =  wallet[-1] - 90
      wallet.append(cost)
      yrgear.append("Orvis")
    elif gsel == "c" and wallet[-1] >= 80:
      cost =  wallet[-1] - 80
      wallet.append(cost)
      yrgear.append("Lamiglas")
    elif gsel == "d" and wallet[-1] >= 70:
      cost =  wallet[-1] - 70
      wallet.append(cost)
      yrgear.append("Gloomis")
    elif gsel == "e" and wallet[-1] >= 50:
      cost =  wallet[-1] - 50
      wallet.append(cost)
      yrgear.append("Uglystik")
    elif gsel == "q":
      break
    else:
      input("Not enough funds    --- Go Fish!\n  Press enter to continue  ")
 
    
def casting():# equip pole and casting loop
  wipit()
  while True:
    while True:
      print("Select a pole to equip")
      lstcnt = 0
      for yr in yrgear:
        print(lstcnt,"|",yr)
        lstcnt+=1
      try:
        eqpol = int(input("\nEnter selection\n"))
        if eqpol < len(yrgear):
          upol = yrgear[eqpol]
          print(upol)
          break
        else:
          wipit()
          print("-----> Enter valid number\n")
      except ValueError:
          wipit()
          print("-----> Enter a number\n")
    wipit()
    print("Pole equipped:",upol)
    cast = input("\n<--- Press c  to cast -----<\n")
    if cast == "c":
      dist = random.randint(1,5)
      if dist >= 5:
        wiped5()
      elif dist > 3:
        wiped4()
      elif dist > 2:
        wiped3()
      elif dist > 1:
        wiped2()
      elif dist > 0:
        wiped1()
      print("Cast distance",dist*10,"Feet")
      if dist > 4:
          print("Good cast!!!")
      break
  return dist,fpole[upol]#returns cast dist


def gfish(x):#jigging loop uses pole value to determine
  odds = x + 6#         how long it takes to hook fish
  jig = 20 - odds
  while True:
    jiggen = input("<--- Press j to jig -----< \n")
    if jiggen == "j":
      jigging1()
      input("<--- Press j to jig -----< \n")
      jigging()
      fihk  = random.randint(jig,odds)
      if jig+1 == fihk:
        print("\n"*5,"   ------------------------------\n\n""       ----- FISH ON !!!!! -----\n")
        fishon()
        break


def reelingr(x):#using casting return int to determine
  cast = x      # reeling cycles
  while True:
    reel = input("<--- Press r to reel in fish -----< \n")
    if reel =="r":
      if cast == 5:
        reeling()
      elif cast == 4:
       reeling1()
      elif cast ==3:
        reeling2()
      elif cast == 2:
        reeling3()
      elif cast == 1:
        reeling4()
      cast -= 1
      if cast == 0:
        gawy = 0
        break
    else:
      jigging()
      print("--- It got away ---")
      gawy = 1
      break
  return gawy


def netting():#net fish determine fish type and size
  while True:#reward applied to walet
    net = input("\n<--- Press n to net your catch -----< \n")
    if net == "n":
      fishsz = random.randint(7,25)
      fishtyp = random.randint(0,4)
      wallet.append(wallet[-1]+fishsz+fishtyp)
      netit()
      if fishsz == 25:
        print("   -- Big fish bonus --$ 25")
        wallet.append(wallet[-1]+25)
      print("Nice catch! You caught a",fishsz,"inch",rfish[fishtyp],"\n   --- $",fishsz+fishtyp,"               Wallet $",wallet[-1])
      prize = str(fishsz)+"inch,"+rfish[fishtyp]
      gdnet = 0
      break
    else:
      prize = "Got away"
      gdnet = 1
      neti()
      print("You missed the fish")
      break
  return prize,gdnet


def lernfish():#fish library
  while True:
    head()
    lnfhmen()
    lrn = input("Enter selection\n")
    if lrn == "a":
      head()
      print("\n"*12)
      with open("lncrapie.txt")as f:
        for line in f:
          line = line.strip()
          print(line)
        input("\nPress enter to continue\n")
    elif lrn == "b":
      head()
      print("\n"*12)
      with open("ltruot.txt")as f:
        for line in f:
          line = line.strip()
          print(line)
        input("\nPress enter to continue\n")
    elif lrn == "c":
      head()
      print("\n"*12)
      with open("lnsmoubas.txt")as f:
        for line in f:
          line = line.strip()
          print(line)
        input("\nPress enter to continue\n")
    elif lrn == "d":
      head()
      print("\n"*12)
      with open("lnbmthbas.txt")as f:
        for line in f:
          line = line.strip()
          print(line)
        input("\nPress enter to continue\n")
    elif lrn == "e":
      head()
      print("\n"*12)
      with open("lntgrmsk.txt")as f:
        for line in f:
          line = line.strip()
          print(line)
        input("\nPress enter to continue\n")
    elif lrn == "q":
      head()#boat n hooks grafic
      menu()#grafix
      break


rfish = ["Crappie","Rainbow Trout","Small Mouth Bass","Big Mouth Bass","Tiger Muskie"]#fish type list

yrcach=[]# fish cought list

wallet = [200]#wallet list

fpole={}#fish pole dictionary
fpole["Fenwick"]=5
fpole["Orvis"]=6
fpole["Lamiglas"]=7
fpole["Gloomis"]=8
fpole["Uglystik"]=9
fpole["Tree branch"]=10

yrgear=["Tree branch"] #your gear list
#tree branch is starter pole
drbt()#starting animation
head()#boat n hooks grafic
menu()#main menu


while True:#main loop
  usel = input("\n\n\nSelect from the menu\n")
  if usel == "b":#buy pole
    pgear()
    head()
    menu()
  elif usel == "a":#go fishing
    casdis,upg = casting()#cast
    gfish(upg)#jig
    gtf = reelingr(casdis)
    if gtf == 1:#lose fish wrong key entered
      menu()#reel
    elif gtf == 0:#didnt lose fish
      bfih,gnet = netting()#net
      if gnet == 1:#missed on netting
        yrcach.append(str(bfih))#you were close so 
        menu()                   # its listed
      elif gnet == 0:#net sucsess
        yrcach.append(str(bfih))#add catch to list
        menu()
  elif usel =="c":#iterate your catch list
    print("\n"*8,"   ----- Your catch -----\n")
    for yr in yrcach:
      print("     ---- ",yr," ----")
    menu()
  elif usel =="s":# save and load game
    usergreq()
  elif usel == "d":#fish library
    lernfish()
  elif usel == "q":#quit game
    dublck = input("Are you sure you want to quit game?\n     y or n\n")
    if dublck == "y":
      break
    else:
      head()#boat n hooks grafic
      menu()#grafix
      continue
  else:
    head()#boat n hooks grafic
    menu()#grafix

