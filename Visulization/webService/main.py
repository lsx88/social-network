#-*- coding:utf-8 -*-

import json
import codecs
import csv
from flask import Flask, render_template,request, abort, Response, jsonify


#configuration
layoutPath = '../layout/'

print "输入文件名，不含后缀名"
filename=raw_input()#likaifu||hubei

result=[]
csvfile = file(layoutPath + filename+'_Example.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    result.append({'id': line[0], 'size': str(float(line[4]) / 2), 'x': str(float(line[1]) / 5)
                         , 'y': str(float(line[2]) / 5), 'color': line[5]})
csvfile.close()

edgesresult=[]
edgescsvfile = file(layoutPath + filename+'_Example_edges.csv', 'rb')
edgesreader = csv.reader(edgescsvfile)
for edgesline in edgesreader:
    edgesresult.append({'id': edgesline[0], 'source': edgesline[1], 'target': edgesline[2], 'weight': edgesline[3]})
edgescsvfile.close()


##网址:localhost:5041/weibo

PORT = 5041
templateFile = 'view.html'
app = Flask(__name__)
#nodes, edges, nodecount, edgecount
@app.route('/weibo', methods=['GET'])
def view():
    return render_template(templateFile, nodes=result, count=len(result),
                           edges=edgesresult, edgescount=len(edgesresult))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=PORT, debug=True)



