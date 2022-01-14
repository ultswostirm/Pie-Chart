from optparse import Values
import pandas as panda
import plotly_express as plot

data=panda.read_csv("data.csv")

pie=plot.pie(data,values="InternetUsers",names="Country",title="Countries Capital Income")

pie.show()
