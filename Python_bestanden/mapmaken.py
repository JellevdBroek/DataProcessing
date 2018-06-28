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

data1 = pd.read_csv("postcodesjvgas.csv")
data = pd.read_csv("data_concat.csv")
postcodes = pd.read_csv("postcodecoords.csv")

jaar = "2018"
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
            if data1[jaar][n] == 0:
                postcode_rates.append("No data available")
            else:
                postcode_rates.append(data1[jaar][n])

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
    title="Amsterdam Standaard jaarverbuik Gas "+str(jaar) + " (m3)", tools=TOOLS,
    x_axis_location=None, y_axis_location=None
)
p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Postcode", "@name"),
    ("SJV Gas", "@rate "),
]

color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, border_line_color=None, location=(0,0))

p.add_layout(color_bar, 'right')

output_file("PostcodeGas"+jaar+".html")
save(p)

show(p)
