import pandas_datareader.data as web
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('ggplot')
start = datetime(2000, 1, 1)
end = datetime(2018, 9, 17)
df = web.DataReader('2160.JP', 'stooq')
df.plot()
plt.show()