telefonkatalog = [] #liste med personer på formatet ["fornavn", "etternavn", "telefonnummer"]

def printMeny ():
    print("-------------Telefonkatalog----------------")
    print("1. legg til ny person")
    print("2. søk opp person eller telefonnummer")
    print("3. vis alle personer")
    print("4. Avslutt")
    print("-------------------------------------------")
    menyvalg = input("skriv in tall for å velge fra menyen:")
    utfoerMenyvalg(menyvalg) 

def utfoerMenyvalg(valgtTall):
        #input returnerer string 
    if(valgtTall== "1"):
        registrerPerson()
    elif(valgtTall== "2"):
        sokPerson()
        printMeny()
    elif(valgtTall== "3"):
        visAllePersoner()
    elif(valgtTall== "4"):
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N")
    if(bekreftelse == "J" or bekreftelse == "j"):
        exit()
                        #Gidder ikke sjekke N fortsetter hvis J
    else:
        nyttForsoek = input("ugyldig valg. Velg et tall mellom 1-4")
        utfoerMenyvalg(nyttForsoek) 

def registrerPerson():
        fornavn = input("Skriv inn fornavn:")
        etternavn = input("Skriv inn etternavn")
        telefonnummer = input("Skriv inn telefonnumer")
        nyRegistrering = [fornavn, etternavn, telefonnummer]
        telefonkatalog.append(nyRegistrering)
                                
        print("{0} {1} er registert med telefonnummer {2}" .format(fornavn, etternavn, telefonnummer))
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny() 
def visAllePersoner():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
        
    else:
        print("*********************************************************")

    for personer in telefonkatalog:
                print("*Fornavn: {:15s} Etternavn: {:15s} telefonnummer: {:8s}" .format(personer[0], personer[1], personer[2]))
                
                print("*********************************************************")

                input("Trykk en tast for å gå tilbake til menyen")
                printMeny()

def sokPerson(): 
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else:
        print("1. søk på fornavn")
        print("2. søk på etternavn")
        print("3. søk på telefonnumer")
        print("4. Tilbake til hovedmenyen")
        sokefelt = input ("skriv inn ønsket søk 1-3, eller 4 for å gå tilbake:")
    if (sokefelt == "1"):
        navn = input ("Fornavn:")
        finnPerson("fornavn", navn)
    elif(sokefelt == "2"):
        navn = input("Etternavn:")
        finnPerson("Etternavn", navn)
    elif(sokefelt == "3"):
        tlfnummer = input("Telefonnummer:")
        finnPerson("telefonnummer", tlfnummer)
    elif(sokefelt == "4"):
        printMeny()
    else:
        print("ugyldig valg. Velg et tall mellom 1-4. ")
        sokPerson()



        #typeSok angir om man søke rpå fornavn eller telefonummer 
def finnPerson(typeSok, sokeTekst):
    for personer in telefonkatalog:
        if(typeSok == "fornavn"):
            if(personer [0] == sokeTekst):
                print("{0} {1} har telefonnummer {2}" .format(personer[0], personer[1], personer[2]))

            else:
                print ("Finner ingen registrerte personer med fornavn " + sokeTekst)
                
                sokPerson()

        elif(typeSok == "etternavn"):
            if(personer [1] == sokeTekst):
                print("Telefonnummer {0} tilhører {1} {2}" .format(personer[2], personer[0], personer[1]))
            else:
                print("Finner ingen registrerte personer med etternavn " + sokeTekst)
                
                sokPerson()

        elif(typeSok == "telefonnummer"):
            if(personer [2] == sokeTekst):
                print("Telefonnummer {0} tilhører {1} {2}" .format(personer[2], personer[0], personer[1]))


            else:
                print("telefonummer " + sokeTekst + "er ikke registrert.")
                sokPerson()
            
printMeny()

