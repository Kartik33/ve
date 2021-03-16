# Variable Elimination for Bayesian Network

### Numpy is required

Initalise the probability tables in init_probelm.py as follows

Initalise a new variable<br>`VariableName = Variable("VariableName")`
 
 Columns: Int<br>`VariableName.domain_size = `

 Initalise Table object<br>`tableName = CPT("TableName")     `            
 
 List of all the variables linked to the table <br>`tableName.linkedVariables = []`
 
 List of all the tables that uses the variable<br>`VariableName.linked_tables = []`
 
 Finally after initialsing all the variabel and table objects provide a variable elimination order in the last line of VE.py<br> `x = VariableElimination(["A" , "D" , "B"])`
 
 Rnu using the command<br> `python ve.py`
 
 ***The output will be the probability of the desired variable after eliminating other variables***
