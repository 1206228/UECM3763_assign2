import pylab as p
import numpy as np

#Define Parameters
alpha=1;
theta=0.064;
sigma=0.27;
R0=3
n_path=1000; #Number of simulation
n=n_partitions=1000;

#Create Brownian Paths
dt=1/n
t=p.linspace(0,1,n+1)[:-1];
dB=p.randn(n_path,n+1)*p.sqrt(dt);
dB[:,0]=0;
B=dB.cumsum(axis=1);
R=p.zeros_like(B);
R[:,0]=R0;

for col in range (n):
    R[:,col+1]=R[:,col]+(theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]
    
#Plot 5 realizations of Mean Reversal Process with labels
R_plot=R[0:5:,:-1]
p.plot(t,R_plot.transpose());
label='Time,t';p.xlabel(label)
label='R(t)';p.ylabel(label)
p.title('5 Realizations for Mean Reversal Process')
p.show()

#Calculations for expectation value for R(1)
R1=p.array(R[:,-1])
E_R1=np.mean(R1)
print('E(R(1))=',E_R1)

#Calculations for P(R(1)>2)
mask=R1>2
P_R1_more_than_2=sum(mask)/len(mask)
print('P(R(1)>2)=',P_R1_more_than_2)