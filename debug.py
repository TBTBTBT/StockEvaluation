import pandas_datareader.data as web
from datetime import datetime
import matplotlib.pyplot as plt
from analyze_candle import CandleAnalyzer
plt.style.use('ggplot')
start = datetime(2000, 1, 1)
end = datetime(2018, 9, 17)
df = web.DataReader('2160.JP', 'stooq')
data = df.iloc[0,[0,1,2,3]]
print(data)
ca = CandleAnalyzer()
result = ca.analyze_candle(data)
print(result)
#df.plot()
#plt.show()