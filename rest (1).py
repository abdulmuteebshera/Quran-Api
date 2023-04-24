
from flask import Flask,jsonify
import json
#Opening and formating file so we can access it accordingly

my_file = open("quran.txt", "r",encoding='utf-8')

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
#print(data_into_list)
my_file.close()




no=[]

verse=[]

for i in data_into_list:
    char = ":"
    indices = [k for k, c in enumerate(i) if c == char]
    
    no.append(i[0:indices[-1]])
    verse.append(i[indices[-1]+1:])
#print(no)
res = dict(zip(no, verse))

# opening the file in read mode
my_file = open("urdu.txt", "r",encoding='utf-8')

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
#print(data_into_list)
my_file.close()

no1=[]

verse1=[]
for i in data_into_list:
    char = ":"
    indices = [k for k, c in enumerate(i) if c == char]
    
    no1.append(i[0:indices[-1]])
    verse1.append(i[indices[-1]+1:])
#print(no)
res1 = dict(zip(no1, verse1))

# opening the file in read mode
my_file = open("eng.txt", "r",encoding='utf-8')

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list1 = data.split("\n")
#print(data_into_list1)
my_file.close()

bigstr = ','.join(data_into_list1)
#print(bigstr)
b=[line.split(',') for line in bigstr.split('   ')]
#print(no)
r2=dict(zip(no, b))
#print(r2)
#print(len(b))

import colorama
from colorama import Fore
# opening the file in read mode
my_file = open("wbw.txt", "r",encoding='utf-8')

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list1 = data.split("\n")
#print(data_into_list1)
my_file.close()
data_into_list2=[]
for i in data_into_list1:
    if i!='   ':
        data_into_list2.append(i)
        
    if i=='   ':
        data_into_list2.append('                   ')
bigstr = ','.join(data_into_list2)

b=[line.split(',') for line in bigstr.split('                   ')]

r1=dict(zip(no, b))
#print(len(r1))
for i in r1:
    x= [ele for ele in r1[i] if ele.strip()]
    r1[i].pop()

app=Flask(__name__)

@app.route('/search/<string:word>/<string:a>')
def search(word,a):


    if word=="arabic":
        results = []
        count = 0
        
        for i in res.values():
            if a in i:
                a1 = list(res.keys())[list(res.values()).index(i)]
                result = {
                    "word": a,
                    "Arabic": res.get(a1),
                    "Urdu": res1.get(a1),
                    "wbw": r2.get(a1)
                }
                results.append(result)
                count += 1
                
        if count < 1:
            results.append({
                "Content:": "No ayah found"
            })



    elif word=="eng":
        results = []
        count = 0
            
        for j in r2.values():
            for i in j:
                if a in i:
                    a1 = list(r2.keys())[list(r2.values()).index(j)]
                    result = {
                        "word": a,
                        "Arabic": res.get(a1),
                        "Urdu": res1.get(a1),
                        "wbw": r2.get(a1)
                    }
                    results.append(result)
                    count += 1
                    
        if count < 1:
            results.append({
                    "Content:": "No ayah found"
                })


    elif word=="urdu":
        results = []
        count = 0
        
        for i in res1.values():
            if a in i:
                a1 = list(res1.keys())[list(res1.values()).index(i)]
                result = {
                    "word": a,
                    "Arabic": res.get(a1),
                    "Urdu": res1.get(a1),
                    "wbw": r2.get(a1)
                }
                results.append(result)
                count += 1
                
        if count < 1:
            results.append({
                "Content:": "No ayah found"
            })
    else:
        results=[]
        results.append({
            "Content:": "language not found"
            })


    json_string = json.dumps(results, ensure_ascii=False)
    return json_string


if __name__=="__main__":
    app.run(debug=True)
