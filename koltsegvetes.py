


def iroda():


    eszkoz=[]
    arai=[]
    darabszam=[]

    for i in range(6):
        eszkoz.append(input("Kérem az eszközt: "))
    
        

    print()

    for i in range(6):
        arai.append(int(input("Kérem az eszköz árát: ")))

    print()

    for i in range(1):
        darabszam.append(int(input("Kérem az eszközök darabszámát az irodában: ")))

    print()

    
    print('Ennyit költöttünk az iroda hálózatra: ', sum(arai), "forintot")

    print('Az Irodában használatos eszközök: ', eszkoz, end=" ")
    

iroda()



print('A következő hálózat a Raktár1')
print()


def raktar1():
    
    eszk=[]
    arak=[]
    dbszam=[]

    for i in range(6):
        eszk.append(input("Kérem az eszközt: "))

    print()

    for i in range(6):
        arak.append(int(input("Kérem az eszköz árát: ")))

    print()

    for i in range(1):
        dbszam.append(int(input("Kérem az eszközök darabszámát az irodában: ")))

    print()

    
    print('Ennyit költöttünk a Raktár1 hálózatra: ', sum(arak), "forintot", end=" ")
    print()
    print('A Raktár1-ben használatos eszközök: ', eszk, end=" ")


raktar1()



print('A következő hálózat a Raktár2')
print()


def raktar2():
    
    eszkz=[]
    araik=[]
    db=[]

    for i in range(6):                                                                                                                                                                                                          
        eszkz.append(input("Kérem az eszközt: "))                                                                                                                                                                                                          
                                                                                                                                                                                                          
    print()                                                                                                                                                                                                          
                                                                                                                                                                                                          
    for i in range(6):
        araik.append(int(input("Kérem az eszköz árát: ")))

    print()

    for i in range(1):
        db.append(int(input("Kérem az eszközök darabszámát az irodában: ")))

    print()

    
    print('Ennyit költöttünk az iroda hálózatra: ', sum(araik), "forintot", end=" ")
    
    print('A Raktár2-ben használatos eszközök: ', eszkz, end=" ")

raktar2()










