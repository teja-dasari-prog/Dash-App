# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:05:06 2025

@author: 243243
"""

import plotly.express as px
from dash import Dash, html
import dash

app=dash.Dash(__name__)
server=app.server

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
fig.show()
plot(fig)


