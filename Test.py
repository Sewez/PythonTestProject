__author__ = 'AeroSpace'
""" Frist question"""
# Reverse list
# tempdata = ["aa", 11, 33, "ff"]
# tempdata.append("stop")
#
# for i, x in enumerate(tempdata):
# 	temp = x
# 	#print temp
# 	tempdata[i] = tempdata[len(tempdata)-i-1]
# 	#print x
# 	tempdata[len(tempdata)-i-1] = temp
#
# 	if i >= (len(tempdata)/2)-1:
# 		break
#
# print tempdata

# Different answer
# tempdata = ["aa", 11, 33, "ff"]
# tempdata.append("stop")
# tempdata = tempdata[::-1]
# print tempdata

""" Second question"""
# Get number of repetitions
# a="abc def abc dfg hjr"
# aList = a.split(' ')
# aDic = {x: 0 for x in aList}
#
# for key in aDic:
# 	for rep in aList:
# 		if rep == key:
# 			aDic[key] += 1
# print aDic

# Different answer
class counter(object):
	def __init__(self, keyword, noofcounts):
		self.keyword = keyword
		self.counts = noofcounts

a="abc def abc dfg hjr"
aList = a.split(' ')
listOfCounter = [counter(x, 0) for x in aList]

# Clear duplicates
clearedList = []
found = False
for i, item in enumerate(listOfCounter):
	for j in clearedList:
		if j.keyword == item.keyword:
			found = True

	if found == False:
		clearedList.append(item)

	found = False

# Count and assign counts
for j in clearedList:
	for i in aList:
		if i == j.keyword:
			j.counts += 1

print map(lambda x: (x.keyword, x.counts), clearedList)
