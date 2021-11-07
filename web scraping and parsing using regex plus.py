import urllib.request
import re

#--------------Scraping--------------------
surl='https://www.summet.com/dmsi/html/codesamples/addresses.html'
res=urllib.request.urlopen(surl)
htmlb=res.read()
htmls=htmlb.decode()

#-------------Parsing----------------------

phoneparse=re.findall('\(\d{3}\) \d{3}-\d{4}',htmls)
namesub=re.sub('i>','  ',htmls)
nameparse=re.findall('  [A-z][a-z]\w* [A-Z][a-z]+',namesub)


find=re.findall(r'Cecilia',htmls)
print('phone',len(phoneparse))
print('name',len(nameparse))

#-----------Writing parsed contents to file--------
f=open('phonecontacte.txt','w')
f.write('     Names          Phone Numbers \n')
for i in range(len(phoneparse)):
    
    f.write(str(i+1)+''+(nameparse[i])+' : '+(phoneparse[i]))
    f.write('\n')
f.close()
    
