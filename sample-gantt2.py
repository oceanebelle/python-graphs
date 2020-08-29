import plotly.express as px
import pandas as pd


df = pd.read_csv("sample-gantt.csv")

fig = px.timeline(
    df, 
    x_start="Start", 
    x_end="Finish", 
    y="Thread",
    title="Show chart of concurrency over time")
fig.show()

fig = px.scatter(
    df, 
    x="Duration", 
    y="Account",
    title="Show duration scatter plot per account")
fig.show()