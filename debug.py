import pandas_datareader.data as web
from datetime import datetime
import matplotlib.pyplot as plt
from analyze_candle import CandleAnalyzer
from analyze_candle import CandleDirectionType
from tqdm import tqdm
#plt.style.use('ggplot')
df = web.DataReader('2160.JP', 'stooq')
#tqdm.pandas(desc = "getting")
#df.progress_apply(lambda x: x)


def lerning_candle(list_,count):
    ca = CandleAnalyzer()
    fig = plt.figure()
    x = list(range(0))
    y = list(range(0))
    for i in range(count):
        data = list_.iloc[i,[0,1,2,3]]
        data2 = list_.iloc[i-1,[0,1,2,3]]
        cs = ca.analyze_candle(data)
        cs2 = ca.analyze_candle(data2)
        x.append(i)
        y.append(data2[3])
        #y.append(cs2.body_length if cs2.direction == CandleDirectionType.POSITIVE else - cs2.body_length)
    del ca
    #ax = fig.add_subplot(1,1,1)
    #ax.scatter(x,y)
    #ax.set_title('first scatter plot')
    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    plt.plot(x,y)
    plt.show()
lerning_candle(df,600)
#df.plot()
#plt.show()