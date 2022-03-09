from enum import Enum, auto
from lib2to3.pgen2.token import MINUS
from tkinter import LEFT
from tkinter.tix import INTEGER
from unittest import result


class Token:

    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LEFT = auto()
        RPARAN = auto()
        LPARAN = auto()


    def __init__(self, type, text) -> None:
        self.type = type
        self.text = text

    def __str__(self) -> str:
        return f'`{self.text}`'

def lex(input):
    result = []

    i=0
    while i<len(input):
        
        if input[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input[i] == '(':
            result.append(Token(Token.Type.LPARAN, '('))
        elif input[i] == ')':
            result.append(Token(Token.Type.RPARAN, ')'))
        else:
            digits = [input[i]]
            for j in range(i+1, len(input)):
                if digits.append(input[j]):
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
    
        i += 1

    return result


def eval(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))


if __name__ == '__main__':
    eval('(13+4)-(12+1)')
