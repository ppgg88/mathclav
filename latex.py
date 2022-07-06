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
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\sqrt{░} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class power():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'^{░}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class indice():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'_{░}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None: 
        self.latex = r""
        return self

class texte():
    def __init__(self) -> None:
        self.content = mathObject()
        self.latex = r'\text{░}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return self.latex.replace('░', str(self.content.str()))
    def destroy(self) -> None:  
        self.latex = r""
        return self

class sqrt_n():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\sqrt[n]{░}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('░', str(self.content[1].str()))
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('n', str(self.content[0].str()))
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex
        return self.latex.replace('░', str(self.content[1].str())).replace('n', str(self.content[0].str()))
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

class integral():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\int_{a}^{b}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('b', str(self.content[1].str()))
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('a', str(self.content[0].str()))
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex
        return self.latex.replace('b', str(self.content[1].str())).replace('a', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class integral2():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\int_{░}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class integral2f():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = '\\oint_{a}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('a', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class integral_double():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\iint_{a}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('a', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class integral_doublef():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = '\oiint_{a}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('a', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class integral_triple():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\iiint_{a}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('a', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class integral_triplef():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = '\\oiiint_{a}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('a', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class parenthese():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r' \left(æ \right) '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('æ', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class parenthese_carre():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r' \left[æ \right] '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('æ', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class crochet():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r' \left\{æ \right\} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('æ', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class union():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\bigcup_{æ1}^{æ2}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', '░')
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('æ1', str(self.content[0].str())).replace('æ2', '░')
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex.replace('æ1', '░').replace('æ2', '░')
        return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class intersection():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\bigcap_{æ1}^{æ2}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', '░')
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('æ1', str(self.content[0].str())).replace('æ2', '░')
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex.replace('æ1', '░').replace('æ2', '░')
        return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class sum():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\sum_{æ1}^{æ2}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', '░')
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('æ1', str(self.content[0].str())).replace('æ2', '░')
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex.replace('æ1', '░').replace('æ2', '░')
        return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class sum1():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\sum_{æ1}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex.replace('æ1', '░')
        return self.latex.replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class prod():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\prod_{æ1}^{æ2}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', '░')
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('æ1', str(self.content[0].str())).replace('æ2', '░')
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex.replace('æ1', '░').replace('æ2', '░')
        return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class prod1():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\prod_{æ1}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex.replace('æ1', '░')
        return self.latex.replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class ln():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\ln{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class log():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\log_{æ1}{\left(æ2\right)}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', '░')
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('æ1', str(self.content[0].str())).replace('æ2', '░')
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex.replace('æ1', '░').replace('æ2', '░')
        return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class exp():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\exp{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class e():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'e^{░} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class cos():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\cos{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self


class sin():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\sin{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class tan():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\tan{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class arccos():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\arccos{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self


class arcsin():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\arcsin{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class arctan():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\arctan{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class vect():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\overrightarrow{░} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self


class lim():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\lim{\left(░\right)} '
    def __add__(self, other) -> None:
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == []:
            return self.latex
        return self.latex.replace('░', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self

class lim1():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\lim_{æ1}{\left(æ2\right)}'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        if self.content[0].content == [] and self.content[1].content != []:
            return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', '░')
        elif self.content[0].content != [] and self.content[1].content == []:
            return self.latex.replace('æ1', str(self.content[0].str())).replace('æ2', '░')
        elif len(self.content[0].content)==0 and len(self.content[1].content)==0:
            return self.latex.replace('æ1', '░').replace('æ2', '░')
        return self.latex.replace('æ2', str(self.content[1].str())).replace('æ1', str(self.content[0].str()))
    def destroy(self) -> None:
        self.latex = r""
        return self