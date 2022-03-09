class Code:
    
    root_name = None
    indent_size = 1
    
    def __init__(self, root_name):
        self.root_name = root_name
        self.elements = []
        
    def printAll(self, indent):
        self.STR = ''
        STR = 'class '+ self.root_name + ':' + '\n\tdef __init__(self):' 
        #print('class '+ self.root_name + ':')
        #print('\tdef __init__(self):')
        for e in self.elements:
            STR = STR + '\n\t\tself.' + e[0] + " = " + e[1]
        return STR


class Field():

    def __init__(self, type, name):
        self.type = type
        self.name = name
    
    
        
class CodeBuilder:
    
    def __init__(self, root_name):
        self.code = Code(root_name)
        
    def add_field(self, type, name):
        self.code.elements.append(Field(type,name))
        return self       

    def __str__(self):
        return self.code.printAll(0)



person = CodeBuilder('Person')\
    .add_field('name', '\"\"')\
    .add_field('age', '0')

print(person)