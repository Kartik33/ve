from init_problem import CPT, variables , tables , np

#print(tables[0].table , "\n\n", tables[1].table)


"""
for i in variables:
    for j in i.linked_tables:
        print(j.name)
"""
class VariableElimination:

    def __init__(self, e_v):
        self.e_v = e_v

    def eliminate(self):
        #print(self.e_v)
        while self.e_v:
            
            var = self.e_v.pop()
            print("eliminating " , var)
            #tables that has eliminating varibale in them
            var_linked_tables = self.get_ev_linked_tables(var)
            for i in var_linked_tables:
                print(i.name)
            broadcast, s, dimen , name , s_dimen, ev_linked_var = self.gen_factor(var_linked_tables , var )
            factor = self.multi(broadcast, var_linked_tables.copy())
            #print(factor , s)
            s = self.sum(factor, s , s_dimen, name)
            print("for this iteration I think you are good " , s.name, s.table)
            
            self.update(var, ev_linked_var, s ,var_linked_tables)
            """
            for i in tables:
                print("after update" , i.name)
            for i in variables:
                print(i.name ,"variables after update")
            """
    def multi(self , broadcast , var_linked_tables):
        t1 = broadcast[var_linked_tables.pop()]
        while var_linked_tables:
            t2 = broadcast[var_linked_tables.pop()]
            t1 = np.multiply(t1,t2)

        return t1

    def sum(self, factor, s, dimen, name, ):
        #print("dimen" , dimen)
        x = CPT(name)
        x.table = np.zeros((dimen))
        for i in s:
            for j in s[i]:
                x.table[i] += factor[j]
        
        return x

    def get_ev_linked_tables(self, e_v):
        
        for i in variables:
            if i.name == e_v:
                return i.linked_tables

    def gen_factor(self , linked_tables,e_v):

        name, dimen, temp_var , s_dimen = self.get_dimen(linked_tables, e_v)
        
        grid = np.ndindex(tuple(dimen))
        #print(name)
        broadcast = {}

        for i in linked_tables:
            broadcast[i] = np.empty((dimen))

        #make a dict of tables for holding the broadcasted list
        s = {}
        for i in grid:
            index = {}
            #assigning the index to the corresponding variable
            for j,a in enumerate(temp_var):
                index[a] = i[j]

            #loop through the broadcast and append the index to every list in the broadcast
            for table in broadcast:
                idx = []
                for j in table.linked_variables:
                    idx.append(index[j])
                broadcast[table][i] = table.table[tuple(idx)]

            for j in variables:
                if j.name == e_v:
                    index.pop(j)
                    abc = []
                    for k in index:
                        abc.append(index[k])
                    abc = tuple(abc)
                    if  abc in s:
                        s[abc].append(i)
                    else:
                        s[abc] = [i]
                    break
       
        return broadcast , s , dimen, name , s_dimen, temp_var

    def get_dimen(self , linked_tables , e_v):
        temp_name = {}
        temp_var = []
        dimen = []
        s_dimen = []

        for i in linked_tables:
            temp_var.extend(i.linked_variables)

        temp_var = set(temp_var)
        
    
        for i in temp_var:
            temp_name[i.name] = i
            
        temp_var = []
        name = ""
        for i in sorted(temp_name.keys()):
            temp_var.append(temp_name[i])
            dimen.append(temp_name[i].domain_size)
            if i != e_v:
                s_dimen.append(temp_name[i].domain_size)
                name = name + temp_name[i].name
        return  name , dimen , temp_var , s_dimen

    def update(self, ev, linked_var , new_table, linked_tables):

        print(ev)
        x = linked_var.copy()
        while x:
            i = x.pop()
            if i.name == ev:
                linked_var.remove(i)
            else:
                for j in i.linked_tables:
                    if j in linked_tables:
                        i.linked_tables.remove(j)
                i.linked_tables.append(new_table)
                        

 

        for a,i in enumerate(variables):
            if i.name == ev:
                variables.pop(a)
        #print("linked tabels are " , linked_tables)
        new_table.linked_variables = linked_var
        #for i in linked_tables:
            #print("linked tables to " , ev ," are " , i.name)
        for i in linked_tables:
            tables.remove(i)
        tables.append(new_table)
        #linke linked_var to the new_table object
        #remove linked tables first and add new_table

if __name__ == "__main__":
    x = VariableElimination(["A" , "B"])
    x.eliminate()
