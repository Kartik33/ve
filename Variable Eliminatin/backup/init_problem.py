from Schema import CPT , Variable 
import numpy as np

A = Variable("A")
A.domain_size = 2
B = Variable("B")
B.domain_size = (2)


t1 = CPT("AB")
t1.table = np.array(((0.1,0.9),(0.2,0.8)))
t1.linked_variables = [A,B]
A.linked_tables = [t1]
B.linked_tables = [t1]


C = Variable("C")
C.domain_size = (2)



t2 = CPT("BC")
t2.table = np.array(((0.3 , 0.7) , (0.6,0.4)))
t2.linked_variables = [B,C]
C.linked_tables = [t2]
B.linked_tables = [t1,t2]

tables = [t1,t2]

variables = [A,B,C]

