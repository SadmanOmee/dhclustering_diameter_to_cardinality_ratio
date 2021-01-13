import plotly.figure_factory as ff
import numpy as np

import plotly.io as pio
pio.renderers.default='browser'

X = [[3, 0], [4, 0], [8, 0], [9, 0], [13, 0], [14, 0], [18, 0], [19, 0]]
X = np.array(X)
#print(X)
names = ['Lion', 'Tiger', 'Cow', 'Goat', 'Penguin', 'Ostrich', 'Eagle', 'Falcon']
fig = ff.create_dendrogram(X, labels=names)
fig.update_layout(width=600, height=500, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig.update_xaxes(range=[0, 100])
fig.show()