class mathObject():
    def __init__(self) -> None:
        self.content = []
    def str(self) -> str:
        tmp = ""
        for i in self.content:
            tmp += str(i.__str__())
        return tmp
    def __add__(self, other) -> None:
        self.content.append(other)
        return self
    
class mathSymbol():
    def __init__(self, char) -> None:
        self.content = [str(char)]
    def __str__(self) -> str:
        return self.content[0]
    def set(self, char)-> None:
        self.content[0] = str(char)


class sqrt():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'\sqrt{æ} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))

class power():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'^{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))

class indice():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'_{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))

class text():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'\text{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str()))

class sqrt_n():
    def __init__(self) -> None:
        self.content = mathObject()
        self.n = mathSymbol('n')
        self.latex = r'sqrt[n]{æ}'
    def __add__(self, other):
        self.content += other
        return self
    def set_n(self, n) -> None:
        self.n.set(n)
        return self
    def __str__(self) -> str:
        return self.latex.replace('æ', str(self.content.str())).replace('n', str(self.n))

if __name__ == '__main__':
    main = mathObject()
    s = sqrt_n()
    s.set_n('3')
    s += mathSymbol('a')
    s += mathSymbol('+')
    s += mathSymbol('b')
    main+=s
    print(main.str())

