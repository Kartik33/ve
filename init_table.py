from classes import *
import numpy as np

t1 = table("ABC")
t1.table = np.random.rand(2,2,2)
t1.headings = ["A","B","C"]

t2 = table("BC")
t2.table = np.random.rand(2,2)
t2.headings = ["B","C"]

               
t3 = table("AB")
t3.table = np.random.rand(2,2)
t3.headings = ["A","B"]


t4 = table("CD")
t4.table = np.random.rand(2,2)
t4.headings = ["D", "C"]