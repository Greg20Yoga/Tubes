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
            print("Skyland City Hotel Jatinangor")
            print("Jatinangor Hotel by Apartemen Taman Melati")
            print("Jatinangor National Golf & Resort")
            print("Emaki Hotel Jatinangor")
            print("Aminda Hotel Jatinangor")
            print("RedDoorz near Jatinangor Town Square")
            print("Puri Khatulistiwa")
            print("La Fasa Syariah Hotel")
            print("RedDoorz Plus near IPDN")
            print("RedLiving Apartemen Easton Park Jatinangor Yunus")
            Hotelj = input("")
        elif h == "b" :
            print("")    
            
    if (g == "c") :
        print("Where would you like to go with a train ?")
        print("Type j for Jatinangor")
        print("Type b for Bandung")
        t = input("")
