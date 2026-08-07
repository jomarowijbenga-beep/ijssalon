from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2): 
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(*korte_lijst)


def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

print (aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden"
print (inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog (mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]
print (laag_en_hoog ([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst): 
    return f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / len(mijn_lijst)} euro."
print (gemiddelde ([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print (meervoudig([10,5,3,2,1,2,9]))

print(combinatie ([10,5,3,2,1,2,9]))