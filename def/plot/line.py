import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from scipy.interpolate import make_interp_spline

def generangeline(agl,bgl):

    amax=np.max(agl)
    amin=np.min(agl)
    bmax=np.max(bgl)
    bmin=np.min(bgl)
    print (float(amax))
    if float(amax)>=float(bmax):
        tmax=amax
    else:
        tmax=bmax
    if float(amin)<=float(bmin):
        tmin=amin
    else:
        tmin=bmin
    tmax=tmax.values
    tmin=tmin.values

    Cy=np.arange(tmin,tmax,0.1)
    return (Cy)


def cyberpunkp(filename, usecols,savefig=False,legend=True,
 fromone=True, smoothp=True, interpolation=100, styleinuse='cyberpunk',
 header=0,cstyle=False,split=False,begin=0,end=0,xlabelname='xname',ylabelname='yname',
 rangeline=False,plotpoints=[0],rangemin=0,rangemax=0):
    
    filename=filename
    header=header
    usecols=usecols
    interpolation=interpolation

    a=pd.read_csv(filename,header=header, usecols=usecols)
    n=len(a.T)
    s=len(a)

    if split==False:
        for i in range(n):
            locals()['a'+str(i)] = a.iloc[0:s,i]

        if fromone==True:
            xold=np.arange(1,(s+1))
        if fromone==False:
            xold=np.arange(s)

    elif split==True:
        for i in range(n):
            locals()['a'+str(i)] = a.iloc[begin:end,i]

        if fromone==True:
            xold=np.arange(1,(s+1))
        if fromone==False:
            xold=np.arange(begin,end)

    fig=plt.figure(figsize=(12, 6), dpi= 300, facecolor='w', edgecolor='w')

    plt.style.use(styleinuse)

    #plt.xlim((-1, 17))
    #plt.ylim((5, 25))
    plt.xticks(color='k')
    plt.yticks(color='k',size=13)
    #plt.xticks([1,2,3,4,5,6,7,8,9,10],size=13)
    #plt.xticks([0, 2, 4, 6, 8,10,12,14,16],['2001', '2003', '2005', '2007', '2009', '2011', '2013', '2015','2017'], color='k')
    
    if smoothp==False:
        if legend==True:
            for i in range(n):
                plt.plot(xold,locals()['a'+str(i)],label=a.columns.values[i], c='k') # marker='o', marker='o',
            plt.legend()

        if legend==False:
            for i in range(n):
                plt.plot(xold,locals()['a'+str(i)], marker='o')
            plt.legend()

    if smoothp==True:
        x_smooth = np.linspace(xold.min(), xold.max(), interpolation)
        for i in range(n):
            locals()['y_smootha'+str(i)] = make_interp_spline(xold, locals()['a'+str(i)], k=2)(x_smooth)
        if legend==True:
            for i in range(n):
                plt.plot(x_smooth,locals()['y_smootha'+str(i)],  label=a.columns.values[i])
            plt.legend()

        if legend==False:
            for i in range(n):
                plt.plot(x_smooth,locals()['y_smootha'+str(i)])
            plt.legend()
            
    plt.xlabel(str(xlabelname),size=18)
    plt.ylabel(str(ylabelname),size=18)
   

    if rangeline==True:
        
        for i in plotpoints:
            Cy=np.arange(rangemin,rangemax,1)
            ix=np.ones(int(len(Cy)))*i
            plt.plot(ix,Cy,'--',c='k',linewidth='0.5') #linewidth='1'


    if cstyle==True:
        mplcyberpunk.add_glow_effects()
    if savefig==True:
        plt.savefig('/work/plotline/result/loss.tif',bbox_inches='tight')
    plt.show()
