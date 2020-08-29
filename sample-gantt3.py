import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import os

if not os.path.exists(".images"):
    os.mkdir(".images")


df = pd.read_csv("sample-gantt.csv")


fig = px.timeline(df, 
    x_start="Start", 
    x_end="Finish", 
    y="Thread",
    text="Data",
    color="Data",
    title="Concurrency plot",
    color_continuous_scale=["red","black"])

# Write the gantt chart
fig.write_image(".images/gantt.png")
fig.write_image(".images/gantt.jpeg")
fig.write_image(".images/gantt.webp")
fig.write_image(".images/gantt.svg")
#fig.write_image(".images/gantt.pdf")


fig = px.scatter(
    df, 
    x="Duration", 
    y="Account",
    color="Data",
    title="Show duration scatter plot per account")

# Write the scatter plot
fig.write_image(".images/scatter.png")
fig.write_image(".images/scatter.jpeg")
fig.write_image(".images/scatter.webp")
fig.write_image(".images/scatter.svg")    


# fig = px.histogram(
#     df,     
#     y="Duration",
#     x="Data",
#     color="Data",
#     marginal='box',
#     barmode="group",
#     barnorm="percent",
#     histfunc='sum',
#     title="Show distribution")

fig = ff.create_distplot(
    [df['Duration']],['duration'], 
    curve_type='normal',     
    show_hist=False)

# Write the distribution plot
fig.write_image(".images/hist.png")
fig.write_image(".images/hist.jpeg")
fig.write_image(".images/hist.webp")
fig.write_image(".images/hist.svg")    


