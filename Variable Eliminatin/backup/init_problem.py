from Schema import CPT , Variable 
import numpy as np

A = Variable("A")
A.domain_size = 2
B = Variable("B")
B.domain_size = (2)

t1 = CPT("A")
t1.table = np.array((0.2,0.8))
t1.linked_variables = [A]


t2 = CPT("AB")
t2.table = np.array(((0.01,0.99),(0.4,0.6)))
t2.linked_variables = [A,B]
A.linked_tables = [t1,t2]



C = Variable("C")
C.domain_size = (2)


t3 = CPT("ABC")
t3.table = np.array(( ((0.99, 0.01),(0.9,0.1)) , ((0.8,0.2),(0.0,1)) ))
t3.linked_variables = [A,B,C]
C.linked_tables = [t3]
B.linked_tables = [t2,t3]

tables = [t3,t1,t2]

variables = [A,B,C]

print("A = Rain, B = Sprinkler, C = GrassWet ")

