import pandas as pd
import json

df = pd.read_csv('test3.csv')
df1 = df ['web_data_uri_sessionized.params']

file = open('metadata3.csv',"w")
file.write('meta title' + ',' + 'meta description' + ','+ 'meta url'+ ',' + 'meta display access level' +'\n')
for i in range (len(df1)):
    x = json.loads(df1[i])
    #print (x["meta.description"])
    file.write(x["meta.title"] + ',')
    file.write (x["meta.description"] + ',')
    file.write (x["meta.og:url"] + ',')
    file.write (x["meta.displayaccesslevel"] + '\n')

file.close()
