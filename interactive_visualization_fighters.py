# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:49:49 2018

@author: Ryan
"""

# Import the necessary modules
from bokeh.io import curdoc, output_file, show
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Slider, HoverTool, Select 
from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row
import numpy as np
import pandas as pd
#import file
df=pd.read_csv('FightMetric_clean.csv')
#reset index
df=df.set_index('Fighter Name')
#set the source data for Bokeh plotting
source=ColumnDataSource(data={
        'x': df['Fighter Height'],
        'y': df['Fighter Reach'],
        'Weight': df['Fighter Weight'],
        'Stance': df['Fighter Stance'],
        'Wins': df['wins'],
        'Loss': df['loss'],
        'tie': df['tie'],
        'Name': df.index})
#set the range of the intial plot
xmin, xmax= min(df['Fighter Reach']), max(df['Fighter Reach'])
ymin, ymax= min(df['Fighter Height']), max(df['Fighter Height'])

#to color everything by stance
stance_list=df['Fighter Stance'].unique().tolist()
color_map= CategoricalColorMapper(factors=stance_list, palette=Spectral6)

#making the inital plot
plot=figure(title='Fighter Height vs Reach', x_range=(xmin, xmax),
            y_range=(ymin, ymax))
plot.circle(x='x', y='y', 
            color=dict(field='Stance', transform=color_map),
            source=source, legend='Stance')
plot.legend.location= 'top_right'

#to add a hover tool
hover = HoverTool(tooltips=[('Fighter Name', '@Name'),
                            ('Fighter Weight', '@Weight'),
                            ('Fighter Record', '@Wins-@Loss-@tie')])
plot.add_tools(hover)

#for updating the plot with the drop downs
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    x = x_select.value
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : df[x],
        'y'       : df[y],
        'Weight': df['Fighter Weight'],
        'Stance': df['Fighter Stance'],
        'Wins': df['wins'],
        'Loss': df['loss'],
        'tie': df['tie'],
        'Name': df.index}
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(df[x])
    plot.x_range.end = max(df[x])
    plot.y_range.start = min(df[y])
    plot.y_range.end = max(df[y])

    # Add title to plot
    plot.title.text = 'Fighter Data for %c %d' %x %y
    
# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['Fighter Height', 'Fighter Weight', 'Fighter Reach', 
             'Fighter SLpM', 'Fighter Striking Accuracy',
             'Fighter SApM', 'Fighter Striking Defence', 
             'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
             'Fighter Take Down Defence', 'Fighter Submission Average', 
             'wins', 'loss', 'total', 'tie', 'win percent'],
    value='Fighter Height',
    title='x-axis data')

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['Fighter Height', 'Fighter Weight', 'Fighter Reach', 
             'Fighter SLpM', 'Fighter Striking Accuracy',
             'Fighter SApM', 'Fighter Striking Defence', 
             'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
             'Fighter Take Down Defence', 'Fighter Submission Average', 
             'wins', 'loss', 'total', 'tie', 'win percent'],
    value='Fighter Reach',
    title='y-axis data')

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(widgetbox(x_select, y_select), plot)
curdoc().add_root(layout)
show(layout)



