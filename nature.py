################################################################################
# parameters
p = [[] for i in range(9)]
n,k,m  = [],[],[]
################################################################################
# functions
def NAN(x):
    for i in range(len(x)):
        if x[i] == '':
            x[i] = 'NAN'
    return x
    
def count_char(char,text=p[1]):
    count = 0
    for i in text:
        if i == char:
            count += 1
    return count
    
def plotcurrent():
    plt.subplot(2,2,1)
    B = count_char('Biological')
    C = count_char('Chemical')
    E = count_char('Earth & Environmental')
    P = count_char('Physical')
    labels = 'Biological','Chemical','Earth & Envionmental','Physical'
    fracs = [B,C,E,P]
    explode =[0.1, 0, 0, 0]
    plt.axes(aspect=1)
    plt.pie(x=fracs,labels=labels,explode=explode,autopct='%3.1f %%',shadow=True,\
    labeldistance=1.1,startangle=90,pctdistance=0.6)
    plt.title("The statistics of current of Nature during 2010-2017")
    plt.show()

def plottype():
    label = 'Article','Forum','Communication','Letter','Review','News and Views','Perspective'
    frac = [count_char('Article',p[7]),count_char('Forum',p[7]),\
    count_char('Brief Communication Arising',p[7])\
    ,count_char('Letter',p[7]),count_char('Review',p[7]),\
    count_char('News and Views',p[7]),count_char('Perspective',p[7])]
    explodes =[0, 0, 0, 0.1, 0, 0, 0]
    plt.axes(aspect=1)
    plt.pie(x=frac,labels=label,explode=explodes,autopct='%3.1f %%',shadow=True,\
    labeldistance=1.1,startangle=90,pctdistance=0.6)
    plt.title("The statistics of paper type of Nature during 2010-2017")
    plt.show()
################################################################################
# main
if __name__ == '__main__':  
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import csv
    import re  
    #regular expression 
    b = re.compile(r'.+\s+(\w*-\w*|\w*)\s+.+')
    c = re.compile(r'(\w*|\w*\s+&\s+\w*)\s+sciences.*')  
     
    with open('all.csv', 'rb') as f:
        readers = csv.reader(f)
        rows = [row for row in readers]
        for line in rows:
            p[0].append(line[0])
            m.append(line[1])
            p[2].append(line[2])
            p[3].append(line[3])
            p[4].append(line[4])
            k.append(line[5])
            p[6].append(line[6])
            p[7].append(line[7])
            p[8].append(line[8])
        f.close()
    for i in k:
        a = re.sub(r'\xa8C',r'-',i)
        n.append(a)
        
    for j in range(len(n)):
        if n[j] == '':
            n[j] = ', NAN ('
            
    for k in n[1:]:
        p[5].append(b.match(k).group(1))
    p[5].insert(0,n[0])
    
    for i in m[1:]:
        p[1].append(c.match(i).group(1))
    p[1].insert(0,'current')
    
    for i in p:
        NAN(i)
################################################################################
    frame = DataFrame(p,index=[p[i][0] for i in range(len(p))],columns=p[2]).T
    frame1=frame.drop('doi',axis=1).drop(frame.ix[0])
    current = frame1.groupby('current')
    typ = frame1.groupby('type')
    #plotcurrent()
    plottype()