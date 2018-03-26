#coding=utf-8

#configuration，预处理
"""
读取结点和边的数据，生成结点的字典，对结点进行从上到下的增序编号，然后用名字查找字典，返回编号
最后将边的数据改写
输入zhi_node(结点)zhi_edge(边)并对结点编号,输出Source(编号)/Target(编号)/Type/Id/Label/Weight
"""

#读取输入的结点，路径
inputNode 		= 'gephiGraph/Zhihu/zhi_node.csv'
#读取输入的边，路径
inputEdge 		= 'gephiGraph/Zhihu/zhi_edge.csv'
#输出，路径
outputForGephi 	= 'gephiGraph/Zhihu/userlayoutFileRel.csv'

#Python的csv模块
import csv

#写csv--在fileName中写data，'wb'--二进制格式打开只用于写入。为什么要用二进制打开？
def writeCsvFile(fileName, data):
	csvfile = file(fileName, 'wb')
	writer = csv.writer(csvfile)

	writer.writerow(('Source','Target','Type','Id','Label','Weight'))
	for d in data:
		writer.writerow((d[0],d[1],d[2],d[3],d[4],d[5]))
	csvfile.close()

#生成字典，count是否为全局变量？
def generateDict(nodes):
	count = 0
	dictionary = dict()
	for i in range(1, len(nodes)):
		dictionary[nodes[i][0]] = i

	return dictionary

#返回字典中指定的值
def findNodeID(name, dictionary):
	return dictionary[name]

#读取csv文件，同样二进制读取
def readCsvFile(fileName):
	csvfile = file(fileName, 'rb')
	reader = csv.reader(csvfile)
	#创建result链表
	result = []
	#每个结果添加到rusult链表的尾巴
	for line in reader:
	    result.append(line)

	csvfile.close() 
	return result

#读取的Node数据存到nodes链表中
nodes = readCsvFile(inputNode)
#生成nodes那么多个数据的已经标号号码的字典
dictionary = generateDict(nodes)
#声明链表
result = []
#读取的Edge数据存到Edges链表中
edges = readCsvFile(inputEdge)

flag = False
for edge in edges:
	if not flag:
		flag = True
		continue
	result.append([dictionary[edge[0]], dictionary[edge[1]], edge[2], edge[3], edge[4], edge[5]])

writeCsvFile(outputForGephi, result)




