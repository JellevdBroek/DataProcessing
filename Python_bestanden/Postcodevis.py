import bokeh
import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure, output_file, save, show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    ColorBar
)
from bokeh.palettes import Viridis8 as palette
from bokeh.plotting import figure

palette.reverse()

def makevis(year, csv, titel, eenheid, label, noav):

    data1 = pd.read_csv(csv)
    postcodes = pd.read_csv("postcodecoords.csv")

    jaar = year
    county_xs = []
    county_ys = []
    postcode_names = []
    postcode_rates = []

    for code in postcodes["POSTCODE"]:     
        postcode_names.append(code)

    for code in postcodes["LON"]:
        jelle = []
        dennis = code.split(",")
        for stukje in dennis:
            jelle.append(int(stukje))
        county_xs.append(jelle)

    for code in postcodes["LAT"]:
        jelle = []
        dennis = code.split(",")
        for stukje in dennis:
            jelle.append(int(stukje))
        county_ys.append(jelle)

    n=0
    for postcode in postcodes["POSTCODE"]:
        for n in range(len(data1[jaar])):
            if data1["POSTCODE"][n] == postcode:
                if data1[jaar][n] == 0 and noav == 1:
                    postcode_rates.append("No data available")
                else:
                    postcode_rates.append(round(data1[jaar][n]))

    postcode_xs = county_xs

    postcode_ys = []
    for ylists in county_ys:
        ylist = []
        for y in ylists:
            ny = 1192 - y
            ylist.append(ny)
        postcode_ys.append(ylist)

    color_mapper = LinearColorMapper(palette=palette)

    source = ColumnDataSource(data=dict(
        x=postcode_xs,
        y=postcode_ys,
        name=postcode_names,
        rate=postcode_rates,
    ))

    TOOLS = "pan,wheel_zoom,reset,hover,save"

    p = figure(
        title= titel + " " +str(jaar) + " " + eenheid, tools=TOOLS,
        x_axis_location=None, y_axis_location=None
    )

    p.image_url( url=[ "adam.png"],
                x=42, y=90, w=1418, h=1015, anchor="bottom_left")

    p.grid.grid_line_color = None

    p.patches('x', 'y', source=source,
            fill_color={'field': 'rate', 'transform': color_mapper},
            fill_alpha=0.7, line_color="white", line_width=0.5)

    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [
        ("Postcode", "@name"),
        (label, "@rate "),
    ]

    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, border_line_color=None, location=(0,0))

    p.add_layout(color_bar, 'right')

    outlen = len(csv) - 4
    out = csv[0:outlen]

    output_file(out + jaar +".html")
    save(p)

    #show(p)

jaarlist = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]

def standaard():
    csvlist = ["postcodesjvelk.csv","postcodesjvgas.csv","postcodesaansluit.csv","postcodewerkans.csv","postcodeszon.csv"]
    eenheidlist = ["(kWh)", "(m3)", "", "", "",]
    titellist = ["Standaard jaarverbruik elektriciteit", "Standaard jaarverbruik gas", "Aantal aansluitingen", "Aantal werkende aansluitingen", "Aantal terugleverende aansluitingen"]
    labellist = ["SJV Elk", "SJV Gas", "Aantal aansluitingen", "Aantal aansluitingen", "Aantal aansluitingen", "Aantal aansluitingen"]
    noavlist = [1,1,0,0,0]
    for n in range(len(csvlist)):
        for jaar in jaarlist:
            makevis(jaar, csvlist[n], titellist[n], eenheidlist[n], labellist[n], noavlist[n])


def makevisperc(year, csv, csv2, titel, eenheid, label, noav):

    data1 = pd.read_csv(csv)
    data2 = pd.read_csv(csv2)
    postcodes = pd.read_csv("postcodecoords.csv")

    jaar = year
    county_xs = []
    county_ys = []
    postcode_names = []
    postcode_rates = []

    for code in postcodes["POSTCODE"]:     
        postcode_names.append(code)

    for code in postcodes["LON"]:
        jelle = []
        dennis = code.split(",")
        for stukje in dennis:
            jelle.append(int(stukje))
        county_xs.append(jelle)

    for code in postcodes["LAT"]:
        jelle = []
        dennis = code.split(",")
        for stukje in dennis:
            jelle.append(int(stukje))
        county_ys.append(jelle)

    n=0
    for postcode in postcodes["POSTCODE"]:
        for n in range(len(data1[jaar])):
            if data1["POSTCODE"][n] == postcode:
                if data2[jaar][n] == 0:
                    postcode_rates.append("No data available")
                elif data1[jaar][n] == 0 and noav == 1:
                    postcode_rates.append("No data available")
                else:
                    postcode_rates.append((data1[jaar][n] * 100 / data2[jaar][n]))

    postcode_xs = county_xs

    postcode_ys = []
    for ylists in county_ys:
        ylist = []
        for y in ylists:
            ny = 1192 - y
            ylist.append(ny)
        postcode_ys.append(ylist)

    color_mapper = LinearColorMapper(palette=palette)

    source = ColumnDataSource(data=dict(
        x=postcode_xs,
        y=postcode_ys,
        name=postcode_names,
        rate=postcode_rates,
    ))

    TOOLS = "pan,wheel_zoom,reset,hover,save"

    p = figure(
        title= titel + " " +str(jaar) + " " + eenheid, tools=TOOLS,
        x_axis_location=None, y_axis_location=None
    )

    p.image_url( url=[ "adam.png"],
                x=42, y=90, w=1418, h=1015, anchor="bottom_left")

    p.grid.grid_line_color = None

    p.patches('x', 'y', source=source,
            fill_color={'field': 'rate', 'transform': color_mapper},
            fill_alpha=0.7, line_color="white", line_width=0.5)

    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [
        ("Postcode", "@name"),
        (label, "@rate " + eenheid),
    ]

    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, border_line_color=None, location=(0,0))

    p.add_layout(color_bar, 'right')

    outlen = len(csv) - 4
    out = csv[0:outlen] + "percentange"

    output_file(out + jaar +".html")
    save(p)

def perczon():
    for year in jaarlist:
        makevisperc(year,"postcodeszon.csv", "postcodewerkanselk.csv", "Percentage Terugleverende aansluitingen", "", "Terugleverende aansluiting %", 0)
        makevisperc(year,"postcodewerkans.csv", "postcodesaansluit.csv", "Percentage werkende aansluitingen", "", "werkende aansluiting %", 0)

def makevisver(year, csv, titel, eenheid, label, noav):

    data1 = pd.read_csv(csv)
    postcodes = pd.read_csv("postcodecoords.csv")

    jaar = year
    county_xs = []
    county_ys = []
    postcode_names = []
    postcode_rates = []

    for code in postcodes["POSTCODE"]:     
        postcode_names.append(code)

    for code in postcodes["LON"]:
        jelle = []
        dennis = code.split(",")
        for stukje in dennis:
            jelle.append(int(stukje))
        county_xs.append(jelle)

    for code in postcodes["LAT"]:
        jelle = []
        dennis = code.split(",")
        for stukje in dennis:
            jelle.append(int(stukje))
        county_ys.append(jelle)

    n=0
    for postcode in postcodes["POSTCODE"]:
        for n in range(len(data1[jaar])):
            if data1["POSTCODE"][n] == postcode:
                if (data1[jaar][n] == 0 and noav == 1) or jaar == "2009":
                    postcode_rates.append("No data available")
                else:
                    oldjaar = str((int(jaar) - 1))
                    postcode_rates.append(round(data1[jaar][n] - data1[oldjaar][n]))

    postcode_xs = county_xs

    postcode_ys = []
    for ylists in county_ys:
        ylist = []
        for y in ylists:
            ny = 1192 - y
            ylist.append(ny)
        postcode_ys.append(ylist)

    color_mapper = LinearColorMapper(palette=palette)

    source = ColumnDataSource(data=dict(
        x=postcode_xs,
        y=postcode_ys,
        name=postcode_names,
        rate=postcode_rates,
    ))

    TOOLS = "pan,wheel_zoom,reset,hover,save"

    p = figure(
        title= titel + " " +str(jaar) + " " + eenheid, tools=TOOLS,
        x_axis_location=None, y_axis_location=None
    )

    p.image_url( url=[ "adam.png"],
                x=42, y=90, w=1418, h=1015, anchor="bottom_left")

    p.grid.grid_line_color = None

    p.patches('x', 'y', source=source,
            fill_color={'field': 'rate', 'transform': color_mapper},
            fill_alpha=0.7, line_color="white", line_width=0.5)

    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [
        ("Postcode", "@name"),
        (label, "@rate "),
    ]

    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, border_line_color=None, location=(0,0))

    p.add_layout(color_bar, 'right')

    outlen = len(csv) - 4
    out = "verschil" + csv[0:outlen]

    output_file(out + jaar +".html")
    save(p)

    #show(p)

def verschil():
    for year in jaarlist:
        makevisver(year, "postcodesaansluit.csv", "Groei aansluitingen", "", "Groei aansluitingen", 0)
        makevisver(year, "postcodeszon.csv", "Groei terugleverende aansluitingen", "", "Groei aansluitingen", 0)

standaard()
perczon()
verschil()