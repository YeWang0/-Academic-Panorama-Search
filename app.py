from flask import Flask
from paper import Paper,Topic
import names
import json
from flask import render_template
from flask import request
import operator

app = Flask(__name__)
with open("data/ML/topic2link.json","r") as fp:
	ML_links=json.load(fp)
with open("data/ML/topic2title.json","r") as fp:
	ML_titles=json.load(fp)
with open("data/IR/topic2link.json","r") as fp:
	IR_links=json.load(fp)
with open("data/IR/topic2title.json","r") as fp:
	IR_titles=json.load(fp)		

with open("data/ML/topic_id.json","r") as fp:
	ML_ids=json.load(fp)
with open("data/IR/topic_id.json","r") as fp:
	IR_ids=json.load(fp)

with open("data/ML/topic_id2label.json","r") as fp:
	ML_idlbs=json.load(fp)
with open("data/IR/topic_id2label.json","r") as fp:
	IR_idlbs=json.load(fp)

# @app.route("/getEmployeeList")
def getTopicList(type):
	# return 'hello'
	# Initialize a employee list
	topicList = []
	if type=='ML':
	# create a instances for filling up employee list
		for i in ML_ids:
		    topic = Topic(i,ML_idlbs[i],len(ML_titles[i]))
		    topicList.append(topic)
	elif type=='IR':
		for i in IR_ids:
		    topic = Topic(i,IR_idlbs[i],len(IR_titles[i]))
		    topicList.append(topic)
	return sorted(topicList, key=operator.attrgetter('papers'),reverse=True)

def getPaperList(i,type):
	paperList = []
	if type=='ML':
		titles=ML_titles[i]
		links=ML_links[i]
	elif type=='IR':
		titles=IR_titles[i]
		links=IR_links[i]
	# create a instances for filling up employee list
	for i in range(0,len(titles)):
	    paper = Paper(titles[i],links[i])
	    paperList.append(paper)
	return paperList

@app.route("/", methods=['POST','GET'])
def home():
	if request.method == 'POST':
		print '*'*50,request.form['type']
		type=request.form['type']
	# if not type:
	else:
		type='IR'	
	data=getTopicList(type)
	# name='ye wang'
	return render_template('index.html', data=data,type=type)

@app.route("/detail/ML/<id>")
def detail_ml(id=0):
	data=getPaperList(id,'ML')
	return render_template('detail.html',data=data,id=id,labels=ML_idlbs[id],title='Machine Learning')

@app.route("/detail/IR/<id>")
def detail_ir(id=0):
	data=getPaperList(id,'IR')
	return render_template('detail.html',data=data,id=id,labels=IR_idlbs[id],title='Information Retrieval')

if __name__ == "__main__":
    app.run()
