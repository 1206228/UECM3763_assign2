import pylab as p
import numpy as np

#Define Parameters
mu=0.1;
sigma=0.26;
S0=39;
n_path=1000; # Number of simulations
n=n_partitions=1000;

#Create Brownian Paths
t=p.linspace(0,3,n+1);
dB=p.randn(n_path,n+1)/p.sqrt(n/3);
dB[:,0]=0;
B=dB.cumsum(axis=1);

#Calculate Stock Prices
nu=mu-sigma*sigma/2.0
S=p.zeros_like(B);
S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#Plot 5 realizations of Geometric Brownian Motion with labels
S_plot=S[0:5]
p.plot(t,S_plot.transpose());
label='Time,t';p.xlabel(label)
label='Stock prices,S(t)';p.ylabel(label)
p.title('5 Runs for Geometric Brownian Motion')
p.show()

#Calculations for expectation value and variance for S3
S3=p.array(S[:,-1])
E_S3=np.mean(S3)
print('E(S(3))=',E_S3)
Var_S3=np.var(S3)
print('Var(S(3))=',Var_S3)

#Calculations for the P(S(3)>39)
mask=S3>39
P_S3_more_than_39=sum(mask)/len(mask)
print('P(S(3)>39)=',P_S3_more_than_39)

#Caluclations for E[S(3)|S(3)>39]
S3_S3_more_than_39=S3*mask
E_S3_S3_more_than_39=sum(S3_S3_more_than_39)/sum(mask)
print('E(S(3)|S(3)>39)=',E_S3_S3_more_than_39)

