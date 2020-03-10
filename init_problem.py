from Schema import CPT , Variable 
import numpy as np

#cloudy
A = Variable("A")
A.domain_size = 2
t1 = CPT("A")
t1.table = np.array(((0.5,0.5)))
t1.linked_variables = [A]
A.linked_tables = [t1]


#sprinkler
B = Variable("B")
B.domain_size = (2)
t2 = CPT("AB")
t2.table = np.array(((0.1,0.9),(0.5,0.5)))
t2.linked_variables = [A,B]


#Rain
C = Variable("C")
C.domain_size = (2)
t3 = CPT("AC")
t3.table = np.array(((0.8,0.2),(0.2,0.8)))
t3.linked_variables = [A,C]

#wetgrass
D = Variable("D")
D.domain_size = 2
t4 = CPT("BCD")
t4.table = np.array((((0.99 , 0.01) , (0.9,0.1)), ((0.9,0.1),(0.0 , 1.0))))
t4.linked_variables = [B,C,D]


C.linked_tables = [t3,t4]
B.linked_tables = [t2,t4]
D.linked_tables = [t4]


tables = [t1,t2,t3,t4]

variables = [A,B,C,D]

