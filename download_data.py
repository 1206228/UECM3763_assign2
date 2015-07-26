from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p
import numpy as np

#Download 5 years daily data for RHB Capital
start=dt(2010,1,1,)
end=dt(2014,12,31)
data=DR("1066.KL",'yahoo',start,end)
print('5 years of daily data for 1066,RHB')
print(data)

#Plot the 5-day moving average for RHB with labels
RHB=DR("1066.KL",'yahoo',start,end)['Close']
mov_avg=pd.rolling_mean(RHB,5)
p.plot(mov_avg)
label='Days';p.xlabel(label)
label='Stock prices';p.ylabel(label)
p.title('5 Days Moving Average Plot for RHB Capital')
p.show()

#Download daily data for FTSEKLCI
klci=DR("^KLSE",'yahoo',start,end)
print('FTSEKLCI closing index')
print (klci)

#Correlation between RHB Capital and KLCI
a=["1066.KL","^KLSE"]
data1=DR(a,'yahoo',start,end)['Close']
correlation=data1.corr()
print('Correlation between RHB Capital and FTSEKLCI=',correlation)