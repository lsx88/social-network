#!/usr/bin/python
#coding=utf-8
layoutPath = '../layout/'

sPath = []
sPath.append('gephiGraph/Weibo/likaifu_Example.gml')
sPath.append('gephiGraph/Weibo/hubei_Example.gml')
sPath.append('gephiGraph/Zhihu/user_Example.gml')

import csv
import os
import networkx as nx

def getEdges(gephi_path):
	graphItems = nx.read_gml(gephi_path)
	#edges类型为edge_list
	edges = graphItems.edges(data = True)
        lay = []
        for e in edges:
            lay.append((e[2]['id'],e[0],e[1],e[2]['value']))

	return lay

for sp in sPath:
	fileName = sp.split('/')[-1]
	# 查找所有的'.gml'并替换为'_edges'，
	name_t = fileName.replace('.gml', '_edges')
	# 输出name_t
	print name_t

	layout = getEdges(sp)

	csvfile = file(layoutPath + name_t + '.csv', 'wb')
	writer = csv.writer(csvfile)
	writer.writerows(layout)

