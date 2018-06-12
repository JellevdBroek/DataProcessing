import pandas as pd
import math


# genereert dataframes voor het type van 2010
def genereer_2010():
    jaren = ["2010"]

    # gaat langs elk jaar van het type 2010 en maakt daar een geschikt dataframe van  
    for jaar in jaren:
        # de namen voor elk jaar worden automatisch gegenereerd
        csv_naam = jaar + ".csv"
        bestandsnaam = "Liander_kleinverbruiksgegevens_0101" + jaar + ".csv"

        with open(csv_naam, "w") as fOut:
            with open(bestandsnaam) as fIn:

                # het csv bestand wordt in een geschikt csv bestand omgezet
                for line in fIn:
                    linelist = list(line)
                    for char in range(len(linelist)):
                        if char == 0 and linelist[char] == ";":
                            fOut.write('0')
                        if linelist[char] == ';' and linelist[char - 1] == ';':
                            fOut.write('0,')
                        elif linelist[char] == ';':
                            fOut.write(',')
                        elif linelist[char] == ',':
                            fOut.write('.')
                        else:
                            fOut.write(linelist[char])
                        if char == len(linelist) - 2 and linelist[char] == ";":
                            fOut.write('0')

            # voor elk jaar wordt een dataframe gemaakt
            if jaar == "2010":
                data_2010 = pd.read_csv(csv_naam, engine="python")

                # een extra collumn met het jaartal wordt toegevoegd
                for line in data_2010:
                    data_2010["Jaar"] = "2010"
                
            elif jaar == "2011":
                data_2011 = pd.read_csv(csv_naam, engine="python")
                for line in data_2011:
                    data_2011["Jaar"] = "2011"
            
            elif jaar == "2012":
                data_2012 = pd.read_csv(csv_naam, engine="python")  
                for line in data_2012:
                    data_2012["Jaar"] = "2012"
                
            elif jaar == "2013":
                data_2013 = pd.read_csv(csv_naam, engine="python")
                for line in data_2013:
                    data_2013["Jaar"] = "2013"
            
            elif jaar == "2014":
                data_2014 = pd.read_csv(csv_naam, engine="python")  
                for line in data_2014:
                    data_2014["Jaar"] = "2014"
            
            elif jaar == "2015":
                data_2015 = pd.read_csv(csv_naam, engine="python")
                for line in data_2015:
                    data_2015["Jaar"] = "2015"
            
            elif jaar == "2016":
                data_2016 = pd.read_csv(csv_naam, engine="python")   
                for line in data_2016:
                    data_2016["Jaar"] = "2016"

            elif jaar == "2017":
                data_2017 = pd.read_csv(csv_naam, engine="python")   
                for line in data_2017:
                    data_2017["Jaar"] = "2017"

            elif jaar == "2018":
                data_2018 = pd.read_csv(csv_naam, engine="python")   
                for line in data_2018:
                    data_2018["Jaar"] = "2018"

    data_2017 = pd.read_csv("2017.csv", engine="python")   
    for line in data_2017:
        data_2017["Jaar"] = "2017"

            
    data_2018 = pd.read_csv("2018.csv", engine="python")   
    for line in data_2018:
        data_2018["Jaar"] = "2018"

    return [data_2010, data_2017, data_2018]


# genereert dataframes voor het type van 2009

def genereer_2009():
    jaren = ["2009","2011","2012","2013","2014","2015","2016" ]

    # gaat langs elk jaar van het type 2009 en maakt daar een geschikt dataframe van.
    for jaar in jaren:
        # de namen voor elk jaar worden automatisch gegenereerd
        csv_naam = jaar + ".csv"
        bestandsnaam = "Liander_kleinverbruiksgegevens_0101" + jaar + ".csv"

        with open(csv_naam, "w") as fOut:
            with open(bestandsnaam) as fIn:
                # het csv bestand wordt in een geschikt csv bestand omgezet
                list = []
                valuelist = []
                for line in fIn:
                    if "WOONPLAATS" in line:
                        list.append(line)
                    elif "AMSTERDAM" in line:
                        valuelist.append(line)
                
                for i in range(len(list)):
                    if list[i].find(','):
                        list[i] = list[i].replace(',', '.')
                    if list[i].find('\t'):
                        list[i] = list[i].replace('\t', ',')
                        fOut.write(list[i])
                        
                for i in range(len(valuelist)):
                    if valuelist[i].find(','):
                        valuelist[i] = valuelist[i].replace(',', '.')
                    if valuelist[i].find('\t'):
                        valuelist[i] = valuelist[i].replace('\t', ',')
                    if valuelist[i].find(',,'):
                        valuelist[i] = valuelist[i].replace(',,',',0,')
                        fOut.write(valuelist[i])
                
                
                # voor elk jaar wordt een dataframe gemaakt met een extra collumnv voor het aantal
                if jaar == "2009":
                    data_2009 = pd.read_csv(csv_naam, engine="python")
                    for line in data_2009:
                        data_2009["Jaar"] = "2009"
                
                elif jaar == "2011":
                    data_2011 = pd.read_csv(csv_naam, engine="python")
                    for line in data_2011:
                        data_2011["Jaar"] = "2011"
                
                elif jaar == "2012":
                    data_2012 = pd.read_csv("2012.csv", engine="python")  
                    for line in data_2012:
                        data_2012["Jaar"] = "2012"
                    
                elif jaar == "2013":
                    data_2013 = pd.read_csv(csv_naam, engine="python")
                    for line in data_2013:
                        data_2013["Jaar"] = "2013"
                
                elif jaar == "2014":
                    data_2014 = pd.read_csv(csv_naam, engine="python")  
                    for line in data_2014:
                        data_2014["Jaar"] = "2014"
                
                elif jaar == "2015":
                    data_2015 = pd.read_csv(csv_naam, engine="python")
                    for line in data_2015:
                        data_2015["Jaar"] = "2015"
                
                elif jaar == "2016":
                    data_2016 = pd.read_csv(csv_naam, engine="python")   
                    for line in data_2016:
                        data_2016["Jaar"] = "2016"

    return [data_2009, data_2011, data_2012, data_2013, data_2014, data_2015, data_2016]


# de lijst met dataframes type 2009 worden aangemaakt
data_list = genereer_2009()
data_list_2 = genereer_2010()
# op de tweede plek wordt het dataframe van 2010 geïnsert.
data_list.insert(1, data_list_2[0])
data_list.append(data_list_2[1])
data_list.append(data_list_2[2])

# de dataframes worden geconcat
data_concat = pd.concat(data_list)

# Er wordt gefilterd op Amsterdam
data_concat2 = data_concat.ix[data_concat["WOONPLAATS"] == "AMSTERDAM"]

del data_concat2['MEETVERANTWOORDELIJKE']
del data_concat2['NETBEHEERDER']
del data_concat2['LANDCODE']
del data_concat2["%Defintieve aansl (NRM)"]
del data_concat2["VERBRUIKSSEGMENT"]
# van de samengevoegde datframe wordt een csv gemaakt
data_concat2.to_csv('data_concat.csv')


print(data_concat2)


    	