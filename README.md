# Variable Elimination for Bayesian Network

To input the probelm instances in init_probelm.py follow the steps below

this will initialise a new variable<br>`VariableName = Variable("VariableName")`
 
 must be an int equal to the number of columns<br>`VariableName.domain_size = `

 this will initalise a new table object <br>`tableName = CPT("TableName")     `            
 
 a list of all the variables linked to this table <br>`tableName.linkedVariables = []`
 
 a list of all the tables that uses this variable<br>`VariableName.linked_tables = []`
 
 Finally after initialsing all the variabel and table objects provide a variable elimination order in the last line of VE.py<br> `x = VariableElimination(["A" , "D" , "B"])`
 
 Rnu using the command<br> `python ve.py`
 
 ***The output will be the probability of the desired variable after eliminating other variables***
