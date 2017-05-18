import json
class Paper:
	def __init__(self,title,link):
		self.title = title
		self.link = link

class Topic:
	def __init__(self,id,labels,papers):
		self.id=id
		self.fid=int(id)+1
		self.labels=labels
		self.papers=papers



# if __name__ == '__main__':
# 	p=Paper('1','2')
# 	print p.toJSON()


