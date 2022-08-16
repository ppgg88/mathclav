# MathClav v0.2  
# by : Team SchnakyX & apparentés (TS&a)
#
# Licence (CC BY-NC-SA 4.0) 2022 - MathClav
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/4.0/ 
# or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
#
# This program is distributed in the hope that it will be useful,
# for any question, please contact us at paul.giroux87@gmail.com

class mathObject():
    def __init__(self) -> None:
        self.content = []
        self.name = "mathObject"
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
    def graphStr(self) -> str:
        tmp = ""
        for i in self.content:
            tmp += str(i.graphStr())
        return tmp
    
class mathSymbol():
    def __init__(self, char) -> None:
        self.content = [str(char)]
        self.imax = -1
    def __str__(self) -> str:
        return self.content[0]
    def set(self, char)-> None:
        self.content[0] = str(char)
    def destroy(self) -> None:
        self.content = [""]
        return self
    def graphStr(self) -> str:
        return self.content[0].replace(r'\ast' , '*').replace(r'\times' , '*').replace(r'\div' , '/')

class sqrt():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\sqrt{░} '
        self.math = "mt.sqrt(a)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('a', str(self.content[0].graphStr()))

class power():
    def __init__(self, view = False) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'^{░}'
        if view:
            self.latex = r'x^{n}'
        else:
            self.math="**a"
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
    def graphStr(self) -> str:
        return self.math.replace('a', str(self.content[0].graphStr()))

class indice():
    def __init__(self, view) -> None:
        self.content = [mathObject()]
        self.imax = len(self.content)-1
        if view:
            self.latex = r'x_{n}'
        else:
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
        return self.latex.replace('░', str(self.content.str())).replace(' ', '').replace(r'\:', r'\: ')
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
        self.latex = r'\frac{æ1}{æ2}'
        self.math = "(æ1)/(æ2)"
    def add_num(self, other):
        self.content_num += other
        return self
    def add_den(self, other):
        self.content_den += other
        return self
    def __str__(self) -> str:
        if(self.content_den.content == [] and self.content_num.content != []):
            return self.latex.replace('æ1', str(self.content_num.str())).replace('æ2', '░')
        if(self.content_den.content != [] and self.content_num.content == []):
            return self.latex.replace('æ2', str(self.content_den.str())).replace('æ1', '░')
        if(self.content_den.content == [] and self.content_num.content == []):
            return self.latex.replace('æ1','░').replace('æ2', '░')
        return self.latex.replace('æ1', str(self.content_num.str())).replace('æ2', str(self.content_den.str()))
    def destroy(self) -> None:
        self.latex = r""
        return self
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr())).replace('æ2', str(self.content[1].graphStr()))

class integral():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject(), mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\int_{æ1}^{æ2} æ3 \: d æ4 \:'
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        x = self.latex
        if self.content[0].content == []:
            x = x.replace('æ1', '░')
        else:
            x = x.replace('æ1', str(self.content[0].str()))
        if self.content[1].content == []:
            x = x.replace('æ2', '░')
        else:
            x = x.replace('æ2', str(self.content[1].str()))
        if self.content[2].content == []:
            x = x.replace('æ3', '░')
        else:
            x = x.replace('æ3', str(self.content[2].str()))
        if self.content[3].content == []:
            x = x.replace('æ4', '░')
        else:
            x = x.replace('æ4', str(self.content[3].str()))
        return x
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
        self.math = '(æ1)'
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

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
        self.math = "mt.ln(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

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
        self.math = "mt.exp(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class e():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'e^{░} '
        self.math = "mt.exp(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class cos():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\cos{\left(░\right)} '
        self.math = "mt.cos(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class sin():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\sin{\left(░\right)} '
        self.math = "mt.sin(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class tan():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\tan{\left(░\right)} '
        self.math = "mt.tan(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class arccos():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\arccos{\left(░\right)} '
        self.math = "mt.acos(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class arcsin():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\arcsin{\left(░\right)} '
        self.math = "mt.asin(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class arctan():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\arctan{\left(░\right)} '
        self.math = "mt.atan(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

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

class matrice():
    def __init__(self, n, m) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        beg = r'\begin{pmatrix}'
        end = r'\end{pmatrix}'
        mil = r''
        for i in range(1,n):
            for j in range(m):
                if j != m-1:
                    mil += r'æ'+str(i)+','+str(j)+' &'
                else :
                    mil += r'æ'+str(i)+','+str(j)+r'\\'
            
        self.latex = beg+mil+end
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        return(self.latex)
    def destroy(self) -> None:
        self.latex = r""
        return self

class system():
    def __init__(self, n, m) -> None:
        self.n = n
        self.m = m
        self.content = []
        for i in range(n):
            for j in range(m):
                self.content.append(mathObject())

        self.imax = len(self.content)-1

        beg = r'\left\{\begin{matrix}'
        end = r'\end{matrix}\right.'
        mil = r''
        for i in range(n):
            for j in range(m):
                if j != m-1:
                    mil += r'æ'+str(i)+','+str(j)+' &'
                else :
                    mil += r'æ'+str(i)+','+str(j)+r'\\'
        self.latex = beg+mil+end
    def __add__(self, other):
        self.content += other
        return self
    def __str__(self) -> str:
        tmp = self.latex
        t = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.content[t].content != []:
                    tmp = tmp.replace('æ'+str(i)+','+str(j), str(self.content[t].str()))
                t += 1
        return(tmp)
    def destroy(self) -> None:
        self.latex = r""
        return self

class binom():
    def __init__(self) -> None:
        self.content = [mathObject(), mathObject()]
        self.imax = len(self.content)-1
        self.latex = r'\binom{æ1}{æ2}'
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
    
    

class norme():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\left\| ░ \right\|'
        self.math = "abs(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))

class norme2():
    def __init__(self) -> None:
        self.content = [mathObject()]
        self.imax = 0
        self.latex = r'\left\Vert ░ \right\Vert'
        self.math = "abs(æ1)"
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
    def graphStr(self) -> str:
        print(self.math)
        return self.math.replace('æ1', str(self.content[0].graphStr()))