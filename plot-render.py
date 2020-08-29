import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd


df = pd.read_csv("data.csv")

fig = px.timeline(df, 
    x_start="Start", 
    x_end="Finish", 
    y="Thread",
    text="Data",
    color="Data",
    title="Concurrency plot",
    color_continuous_scale=["red","black"])
fig.show()    

fig = px.scatter(
    df, 
    x="Duration", 
    y="Account",
    color="Data",
    title="Show duration scatter plot per account")
fig.show()

fig = ff.create_distplot(
    [df['Duration']],['duration'], 
    curve_type='normal',     
    show_hist=False)

fig.show()