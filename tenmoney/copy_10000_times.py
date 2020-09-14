#coding=utf-8

"""
author:Shine
function:to do performace testing, 10000 times the param
"""
def copy_1000_times():
	f = open("out.txt","w")
	num = 1
	while num <= 10000:
		f.write(",{\"staffId\": \"90d62a0d736d47848b9d9ea17b4c59d7\",\"target\": 1}\n")
		num = num + 1
	
copy_1000_times();
b = input("p")
