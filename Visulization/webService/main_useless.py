#-*- coding:utf-8 -*-

import json
import codecs

#configuration
layoutPath = '../layout/'
detailPath = '../generateGraph/gephiGraph/Weibo/Details/'
#read .csv
layoutFile = []
layoutFile.append('likaifu_Example.csv')
layoutFile.append('hubei_Example.csv')
layoutFile.append('user_Example.csv')

loFile = []
loFile.append('likaifu_Example_edges.csv')
loFile.append('hubei_Example_edges.csv')
loFile.append('user_Example_edges.csv')

detailFile = []
detailFile.append('likaifu_details.csv')
detailFile.append('hubei_details.csv')

route = []
route.append('/weibo/likaifu')
route.append('/weibo/hubei')
route.append('/zhihu/user')

PORT = 5041
templateFile = 'view.html'

user_description = {}

with codecs.open('../generateGraph/gephiGraph/Weibo/Details/hubei_details.csv', "r", encoding="gbk", errors="replace") as f:
    for line in f.readlines():
        data = line.split(',')
        user_description[data[1]] = data[12] if len(data) > 12 else None

with open('user_description.json', 'w+') as f:
    f.write(json.dumps(user_description, encoding='utf-8', indent=2, separators=(',', ': ')).decode('unicode-escape').encode('utf-8'))

test = {}

with codecs.open('../generateGraph/gephiGraph/Weibo/Details/hubei_details.csv', "r", encoding="gbk", errors="replace") as f:
    for line in f.readlines():
        data = line.split(',')
        test[data[1]] = data[7] if len(data) > 7 else None

with open('test.json', 'w+') as f:
    f.write(json.dumps(test, encoding='utf-8', indent=2, separators=(',', ': ')).decode('unicode-escape').encode('utf-8'))

user_name = {}

with codecs.open('../generateGraph/gephiGraph/Weibo/Details/hubei_details.csv', "r", encoding="gbk", errors="replace") as f:
    for line in f.readlines():
        data = line.split(',')
        #print(len(data) > 11, data[2])
        user_name[data[1]] = data[11] if len(data) > 11 else None


with open('user_name.json', 'w+') as f:
    f.write(json.dumps(user_name, encoding='utf-8', indent=2, separators=(',', ': ')).decode('unicode-escape').encode('utf-8'))

from flask import Flask, render_template,request, abort, Response, jsonify
import csv

result = dict()

for f in layoutFile:
    csvfile = file(layoutPath + f, 'rb')
    reader = csv.reader(csvfile)
    result[f] = []

    for line in reader:       
        result[f].append({'id':line[0], 'size':str(float(line[4])/2), 'x':str(float(line[1])/5)
                             , 'y':str(float(line[2])/5), 'color':line[5]})
    csvfile.close()

edgesresult = dict()

for l in loFile:
    edgescsvfile = file(layoutPath + l, 'rb')
    edgesreader = csv.reader(edgescsvfile)
    edgesresult[l] = []

    for edgesline in edgesreader:
        edgesresult[l].append({'id':edgesline[0],'source':edgesline[1], 'target':edgesline[2], 'weight':edgesline[3]})
    edgescsvfile.close()

detailresult = dict()

flag = 0
for d in detailFile:
    detailcsvfile = file(detailPath+d,'rb')
    detailreader = csv.reader(detailcsvfile)
    detailresult[d] = []
    for detail in detailreader:
        detailresult[d].append({'lmid':detail[0],'mid':detail[1],'uid':detail[2],'t':detail[3],'relay':detail[4]
                                   ,'like':detail[5],'comment':detail[6],'content':detail[7],'fans':detail[8]
                                   ,'ucount': detail[9],'ulike':detail[10],'uname':detail[11],'ud':detail[12]
                                   ,'ug':detail[13],'up':detail[14],'uc':detail[15],'verified':detail[16]
                                   ,'v_r':detail[17],'u_l':detail[18]})
    detailcsvfile.close()

app = Flask(__name__)

#nodes, edges, nodecount, edgecount
@app.route(route[0], methods=['GET'])
def weibo_likaifu_view():
    return render_template(templateFile, nodes=result[layoutFile[0]], count=len(result[layoutFile[0]]),
                           edges=edgesresult[loFile[0]], edgescount=len(edgesresult[loFile[0]]))

@app.route(route[1], methods=['GET'])
def weibo_hubei_view():
    return render_template(templateFile, nodes=result[layoutFile[1]], count=len(result[layoutFile[1]]),
                           edges=edgesresult[loFile[1]], edgescount=len(edgesresult[loFile[1]]))

@app.route(route[2], methods=['GET'])
def zhihu_user_view():
    return render_template(templateFile, nodes=result[layoutFile[2]], count=len(result[layoutFile[2]]),
                           edges=edgesresult[loFile[2]], edgescount=len(edgesresult[loFile[2]]))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=PORT, debug=True)
