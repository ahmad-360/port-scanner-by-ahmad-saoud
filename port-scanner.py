#Hi This Tool Devlopped By The Litlle Hacker
#This tool is intended for learning only and for protection any activity outside of these things. 
#We will take no responsibility.
                                        #And thank you for your understanding.





###################### LIBRARYS #############################################
import socket 
import os
import sys
from time import *
from V7xStyle import Animation
##################### Designer ################################################
os.system('clear')
An = Animation
text =  '''   
 ____            _             ____                                  
|  _ \ ___  _ __| |_          / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) / _ \| '__| __|  _____  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_  |_____|  ___) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__|         |____/ \___\__,_|_| |_|_| |_|\___|_|      by Ahmed Saoud "The Little-Hacker"
                                                                   Friends For ever "Moroccco and Algeria"

'''
An.SlowIndex(text,t=0.005)
                                                                  

h= print ("                                                                                                                                    ")
license = print('''Hello this tool was developed by The Little-Hacker and aims to learn and protect only, any activity outside of these terms will not take any responsibility..!''')

li =   print("And thank you for your understanding.")
H = print ("                                                                                                                                    ")
l= input("Will you agree to these terms?  Y/n ")
h=print("                                                                ")

if l == 'Y'or 'y': 
    ip = input ("====> ENTER IP YOU WANT TO SCAN: ")


    An = Animation 

    An.DL(AT=['B#│', 'G#█', 'C#▒', 'B#│'],
       
    text = 'Wait Bro ...',t=0.05,width =50)

    print("Scannig Start..  %s Please Wait.. "%ip)
    sleep(1)
###################### SCANNIG ##########################################
    try:
         for port in range(1,6553):
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             if(s.connect_ex((ip,port))==0):
                 try:
                      serv=socket.getservbyport(port)
                 except socket.error:
                     serv="Unknown Service"
                 print("[+]Port %s Open Service: %s"%(port,serv))


         print("Scannig Complete ")
    except KeyboardInterrupt:
         print(" See You Soon...!")
###################### FINISH ###############################################
else:
    exit()
  

