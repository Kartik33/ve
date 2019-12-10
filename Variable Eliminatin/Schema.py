class CPT:
    def __init__(self,name):
        self.name = name

    table = None
    linked_variables = None
    domain = None


class Variable:
    def __init__(self, name):
        self.name = name

    linked_tables = None
    domain_size = None
