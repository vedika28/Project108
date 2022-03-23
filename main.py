import pandas as pd, plotly.figure_factory as pff

data=pd.read_csv('d.csv')
fig=pff.create_distplot([data['Avg Rating']],['Average Rating'])
fig.show()