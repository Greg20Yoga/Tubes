#Screen
print("Type 1 to turn on ")
print("Type 0 to turn off ")
Screen = int(input(""))
Hj = [0 for o in range(10)]
if Screen == 1 :
    print("Welcome to loka")
    print("Where do you wish to go ?")
    print("Type a if you want to find an apartment")
    print("Type b if you want to find a hotel")
    print("Type c if you want to use a train")
    print("Type d if you want to use a damri")
    print("Type e if you want to use an arnes")
    g = input(" ")  
    if (g == "b") :
        print("Where is the location :")
        print("Type j for Jatinangor")
        print("Type b for Bandung")
        h = input("")
        if h == "b" :
            

        if h == "j" :
            Jhotel = ["Skyland City Hotel Jatinangor","Jatinangor Hotel by Apartemen Taman Melati","Jatinangor National Golf & Resort","Emaki Hotel Jatinangor","Aminda Hotel Jatinangor","RedDoorz near Jatinangor Town Square","Puri Khatulistiwa","La Fasa Syariah Hotel", "RedDoorz Plus near IPDN","RedLiving Apartemen Easton Park Jatinangor Yunus"]
            print(f"1. {Jhotel[0]}")
            print(f"2. {Jhotel[1]}")
            print(f"3. {Jhotel[2]}")
            print(f"4. {Jhotel[3]}")
            print(f"5. {Jhotel[4]}")
            print(f"6. {Jhotel[5]}")
            print(f"7. {Jhotel[6]}")
            print(f"8. {Jhotel[7]}")
            print(f"9. {Jhotel[8]}")
            print(f"10. {Jhotel[9]}")
            hj = input("")
            
            
            
        elif h == "b" :
            Bhotel = ["The Gaia Hotel Bandung",]
            print("")    
            
    if (g == "c") :
        print("Where would you like to go with a train ?")
        print("Type j for Jatinangor")
        print("Type b for Bandung")
        t = input("")
