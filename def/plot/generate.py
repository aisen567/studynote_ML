import numpy as np
import scipy.stats as scist
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def nordata(genedata=False, filename='/work/1000.csv', header=0, usecols1=[1],usecols2=[2], datatype='ind',
mu1=30, sigma1=2, samplen1=50, sn1s=1, sn1b=1, 
mu2=28, sigma2=1, samplen2=50, sn2s=1, sn2b=1):
    #real data
    if genedata==False:
        
        data1=pd.read_csv(filename,header=header, usecols=usecols1)
        data2=pd.read_csv(filename,header=header, usecols=usecols2)
        data1=data1.values.flatten()
        data2=data2.values.flatten()
        w1,p1=scist.shapiro(data1)
        print ('data1: \nmu:' + str(np.mean(data1))+ ' sigma:'+str(np.std(data1))+' median:'+str(np.median(data1))+ ' 25%:'+str(np.quantile(data1,0.25,interpolation='lower')) +' 75%:'+str(np.quantile(data1,0.75,interpolation='higher')))
        w2,p2=scist.shapiro(data2)
        print ('data2: \nmu:' + str(np.mean(data2))+ ' sigma:'+str(np.std(data2))+' median:'+str(np.median(data2))+ ' 25%:'+str(np.quantile(data2,0.25,interpolation='lower')) +' 75%:'+str(np.quantile(data2,0.75,interpolation='higher')))
        
        print ('\nPerform the Shapiro-Wilk test for normality: ', '\ndata1:','\nstatics: ' +str(w1),'\np-value: ' +str(p1))
        print ('data2:','\nstatics: ' +str(w2),'\np-value: ' +str(p2))

    #fake data
    elif genedata==True:
    
        rangebegin1=(mu1-sn1s*sigma1)
        rangeend1=(mu1+sn1b*sigma1)
        ntip1=round(samplen1/4)
        tip1=np.random.uniform(rangebegin1,rangeend1,ntip1)
        data1=np.random.normal(mu1, sigma1,(samplen1-ntip1))
        data1=np.append(data1,tip1)
        data1=abs(data1)
        #np.savetxt('/home/jovyan/work/results/data1.txt',data1, fmt='%.6f', delimiter=',')
        #plt.subplot(121)
        #plt.hist(data1)
        w1,p1=scist.shapiro(data1)
        print ('data1: \nmu:' + str(np.mean(data1))+ ' sigma:'+str(np.std(data1))+' median:'+str(np.median(data1))+ ' 25%:'+str(np.quantile(data1,0.25,interpolation='lower')) +' 75%:'+str(np.quantile(data1,0.75,interpolation='higher')))
        #print ('Perform the Shapiro-Wilk test for normality: ', '\n\ndata1:','\nstatics: ' +str(w1),'\np-value: ' +str(p1))
        

        rangebegin2=(mu2-sn2s*sigma2)
        rangeend2=(mu2+sn2b*sigma2)
        ntip2=round(samplen2/4)
        tip2=np.random.uniform(rangebegin2,rangeend2,ntip2)
        data2=np.random.normal(mu2, sigma2,(samplen2-ntip2))
        data2=np.append(data2,tip2)
        data2=abs(data2)
        #np.savetxt('/home/jovyan/work/results/data2.txt',data2, fmt='%.6f', delimiter=',')
        #plt.subplot(122)
        #plt.hist(data2)
        w2,p2=scist.shapiro(data2)
        print ('data2: \nmu:' + str(np.mean(data2))+ ' sigma:'+str(np.std(data2))+' median:'+str(np.median(data2))+ ' 25%:'+str(np.quantile(data2,0.25,interpolation='lower')) +' 75%:'+str(np.quantile(data2,0.75,interpolation='higher')))
        
        print ('\nPerform the Shapiro-Wilk test for normality: ', '\ndata1:','\nstatics: ' +str(w1),'\np-value: ' +str(p1))
        print ('data2:','\nstatics: ' +str(w2),'\np-value: ' +str(p2))


    #normal distribution
    if p2>=0.05 and p1>=0.05:
        print ('\nnormal distribution')
        # levene
        levenestatistic,levenepvalue=scist.levene(data1, data2)
        if datatype=='ind':
            
            if levenepvalue>=0.05:
                tteststatistic,ttestpvalue=scist.ttest_ind(data1,data2)
                print ('independent-sample t test')
            
            #Heterogeneity of variance
            elif levenepvalue<0.05:
                tteststatistic,ttestpvalue=scist.ttest_ind(data1,data2,equal_var = False)
                print ("Heterogeneity of variance, use T' test")
            
            print ('\nstatics: ' +str(tteststatistic),'\np-value: ' +str(ttestpvalue))
        
        elif datatype=='rel':
            tteststatistic,ttestpvalue=scist.ttest_rel(data1,data2)
            print ('paired-sample test','\n\nstatics: ' +str(tteststatistic),'\np-value: ' +str(ttestpvalue))


    #non-normal distribution
    else:
        print ('\nnon-normal distribution')
        
        if datatype=='ind':

            # wilcox秩序和检验
            if samplen1<20 or samplen2<20 :
                print ('\nWilcoxon rank-sum test')
                wstatistic,wpvalue=scist.ranksums(data1,data2)
                print ('\nstatics: ' +str(wstatistic),'\np-value: ' +str(wpvalue))

            # Mann-Whitney U检验
            else:
                print ('\nMann–Whitney U test')
                wstatistic,wpvalue=scist.mannwhitneyu(data1,data2)
                print ('\nstatics: ' +str(wstatistic),'\np-value: ' +str(wpvalue))

        elif datatype=='rel':
            # Wilcox检验
            print ('Wilcoxon signed-rank test ')
            wstatistic,wpvalue=scist.wilcoxon(data1,data2, zero_method='wilcox', correction=False)
            print ('\nstatics: ' +str(wstatistic),'\np-value: ' +str(wpvalue))

    return data1, data2

def violinconcat(crange,a0=([1,2,3]),b0=([1,2,3]),a1=([1,2,3]),b1=([1,2,3]),a2=([1,2,3]),b2=([1,2,3]),
a3=([1,2,3]),b3=([1,2,3]),a4=([1,2,3]),b4=([1,2,3]),a5=([1,2,3]),b5=([1,2,3])):  #a0,b0,a1,b1
    
    numdata0=np.zeros(len(a0))
    numdata1=np.ones(len(b0))

    wholedata=[]
    #print (a0)
    for i in range(crange):
        locals()['measurement'+str(i)]=np.zeros(len(a0))+int(i)

    for j in range(crange):
        locals()['cdata'+str(j)]=pd.DataFrame({'group':numdata0,'measurement':locals()['measurement'+str(j)],'data': locals()['a'+str(j)]})
        
        locals()['cdatb'+str(j)]=pd.DataFrame({'group':numdata1,'measurement':locals()['measurement'+str(j)],'data': locals()['b'+str(j)]})
        
        wholedata.append(locals()['cdata'+str(j)])
        wholedata.append(locals()['cdatb'+str(j)])
        
    wholedata=pd.concat(wholedata,axis=0)
    return wholedata  

def violinhalfplot(group,measurement,plotdata,wholedata,groupname=['A','B'],savefig=False,zerol='shit',onel='fuck off'):
    plt.figure(figsize=(12, 6),dpi=900)

    tips = sns.load_dataset('tips')
    ax=sns.violinplot(x=measurement, y=plotdata, hue=group,
                   data=wholedata,split=True)

    legend = ax.legend()  
    legend.texts[0].set_text(zerol)
    legend.texts[1].set_text(onel)

    plt.xlabel('Group', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    groupsn=np.arange(0,(np.max(group)+1),1)

    plt.xticks(groupsn,groupname)

    if savefig==True:
        plt.savefig('/home/jovyan/work/results/viohalf.png')
    

def vioscahalfplot(group,measurement,plotdata,wholedata,groupname=['A','B'],savefig=False,zerol='shit',onel='fuck off',usetitle=False, newtitle = 'My title'):
    plt.figure(figsize=(12, 6),dpi=900)
    tips = sns.load_dataset('tips')
    axa=sns.violinplot(x=measurement, y=plotdata, hue=group,
                   data=wholedata,split=True)

    axa=sns.stripplot(x=measurement, y=plotdata, hue=group, data=wholedata,
              dodge=True,split=True,
              jitter=True,palette=sns.color_palette("plasma_r",n_colors=3), linewidth=1,
              alpha=0.35,marker='D',size=5, edgecolor='white') #h
    
    legend = axa.legend()  
    legend.texts[0].set_text(zerol)
    legend.texts[1].set_text(onel)
    legend.texts[2].set_text(zerol)
    legend.texts[3].set_text(onel)
    
    if usetitle==True:
        legend.set_title(newtitle)

    plt.xlabel('Group', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    groupsn=np.arange(0,(np.max(group)+1),1)

    plt.xticks(groupsn,groupname)

    if savefig==True:
        plt.savefig('/home/jovyan/work/results/vio&sca.png')

def normaldataconcat(a1,b1,a2,b2,a3,b3,a4,b4):
    numdata1=np.zeros(len(a1))
    numdata2=np.ones(len(b1))

    cdata1=pd.DataFrame({'group':numdata1,'data': a1})
    cdatb1=pd.DataFrame({'group':numdata2,'data': b1})

    cdata2=pd.DataFrame({'data': a2})
    cdatb2=pd.DataFrame({'data': b2})

    cdata3=pd.DataFrame({'data': a3})
    cdatb3=pd.DataFrame({'data': b3})    

    cdata4=pd.DataFrame({'data': a4})
    cdatb4=pd.DataFrame({'data': b4})


    dataf1=pd.concat([cdata1, cdatb1],axis=0)
    dataf2=pd.concat([cdata2, cdatb2],axis=0)
    dataf3=pd.concat([cdata3, cdatb3],axis=0)
    dataf4=pd.concat([cdata4, cdatb4],axis=0)

    wholedata=pd.concat([dataf1, dataf2, dataf3, dataf4],axis=1)
    np.savetxt('/home/jovyan/work/results/alldata.txt',wholedata, fmt='%.6f', delimiter=',')
