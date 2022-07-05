class mathObject():
    def __init__(self) -> None:
        self.content = []
    def str(self) -> str:
        tmp = ""
        for i in self.content:
            tmp += str(i.__str__())
        return tmp
    def __add__(self, other):
        self.content.append(other)
        return self
    def add(self, other, i):
        self.content.insert(i, other)
        return self
    def destroy(self, i = -1) -> None:
        if i == -1:
            self.content.pop(len(self.content)-1)
        else:
            self.content.pop(i-1)
        return self
    
class mathSymbol():
    def __init__(self, char) -> None:
        self.content = [str(char)]
    def __str__(self) -> str:
        return self.content[0]
    def set(self, char)-> None:
        self.content[0] = str(char)
    def destroy(self) -> None:
        self.content = [""]
        return self

class sqrt():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'\sqrt{æ} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content.content == []:
            return self.latex
        return self.latex.replace('æ', str(self.content.str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class power():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'^{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class indice():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'_{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))
    def destroy(self) -> None: 
        self.latex = r""
        return self

class text():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'\text{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))
    def destroy(self) -> None:  
        self.latex = r""
        return self

class sqrt_n():
    def __init__(self) -> None:
        self.content = mathObject()
        self.n = mathSymbol('n')
        self.latex = r'\sqrt[n]{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def set_n(self, n) -> None:
        self.n.set(n)
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str())).replace('n', str(self.n))
    def destroy(self) -> None:
        self.latex = r""
        return self

class frac():
    def __init__(self) -> None:
        self.content_num = mathObject()
        self.content_den = mathObject()
        self.content = [self.content_num, self.content_den]
        self.imax = len(self.content)-1
        self.latex = r'\frac{æ}{b}'
    def add_num(self, other):
        self.content_num += other
        return self
    def add_den(self, other):
        self.content_den += other
        return self
    def __str__(self) -> str:
        if(self.content_den.content == [] and self.content_num.content != []):
            return self.latex.replace('æ', str(self.content_num.str())).replace('b', 'æ')
        if(self.content_den.content != [] and self.content_num.content == []):
            return self.latex.replace('b', str(self.content_den.str())).replace('æ', 'æ')
        if(self.content_den.content == [] and self.content_num.content == []):
            return self.latex.replace('b','æ').replace('æ', 'æ')
        return self.latex.replace('æ', str(self.content_num.str())).replace('b', str(self.content_den.str()))
    def destroy(self) -> None:
        self.latex = r""
        return self


if __name__ == '__main__':
    main = mathObject()
    s = sqrt_n()
    s.set_n('3')
    s += mathSymbol('a')
    s += mathSymbol('+')
    s += mathSymbol('b')
    main+=s
    main+=mathSymbol('+')
    main+=mathSymbol('c')
    print(main.str())
    main.destroy()
    main+=mathSymbol('d')
    print(main.str())
