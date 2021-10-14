import urllib.request
import re

surl='https://www.summet.com/dmsi/html/codesamples/addresses.html'
res=urllib.request.urlopen(surl)
htmlb=res.read()
htmls=htmlb.decode()

phoneparse=re.findall(r'\(\d{3}\) \d{3}-\d{4}',htmls)
namesub=re.sub('i>','  ',htmls)
nameparse=re.findall(r'  [A-z][a-z]\w* [A-Z][a-z]+',namesub)


find=re.findall(r'Cecilia',htmls)
print('phone',len(phoneparse))
print('name',len(nameparse))
print('     Names               Phone Numbers')
for i in range(len(phoneparse)):
    
    print((i+1),'',nameparse[i],' : ',phoneparse[i])
    
