"""
Partial transpiler from Lisp-like language to Folders (https://esolangs.org/wiki/Folders).
"""

import os
import os.path
import random

class Path(os.PathLike):
    __path: str

    def __init__(self, path_like: any):
        self.__path = path_like

    def __truediv__(self, path_like: any):
        return Path(os.path.join(self.__path, str(path_like)))

    def __str__(self) -> str:
        return self.__path

    def __repr__(self) -> str:
        return f"Path({str(self)})"

    def __fspath__(self) -> str:
        return self.__path

SYS_WORDS = ["bin", "boot", "default", "dev", "mnt", "etc", "home", "opt", "proc", "root", "run", "srv", "sys", "tmp", "usr", "var"]
class Lisp2Folders():
    __base_dir: Path

    def __init__(self, base_dir: str="./"):
        if not os.path.exists(base_dir):
            self._mkdir(base_dir)

        self.__base_dir = Path(base_dir)

    def build(self, expression):
        self._build_any(self.__base_dir, expression)

    def _parse_next_expression(self, text):
        stack = 0

        for i, c in enumerate(text):
            if c == "(":
                stack += 1
            elif c == ")":
                stack -= 1
            
            if stack == 0:
                return text[1:i].lstrip(), text[i+1:].lstrip()

        return None, None

    def _parse_expressions(self, text):
        expressions = []

        remainder = text.strip()
        while len(remainder) > 0:
            expression, remainder = self._parse_next_expression(remainder)

            if not expression: break

            expressions.append(expression)

        return expressions

    def _parse_next_word(self, text):
        return text[:text.index(" ")].lstrip(), text[text.index(" "):].lstrip()

    def _get_names(self, count):
        return sorted(random.sample(SYS_WORDS, k=count))

    def _build_any(self, base_dir: Path, expressions):
        for expression in self._parse_expressions(expressions):
            operator, expression = self._parse_next_word(expression)

            if operator == "dir":
                self._build_dir(base_dir, expression)
            elif operator == "print":
                self._build_print(base_dir, expression)
            elif operator == "literal":
                self._build_literal(base_dir, expression)
            else:
                raise Exception(f"Unimplemented operator `{operator}`.")

    def _mkdir(self, dir: Path):
        os.mkdir(dir)
        return dir

    def _mkdirn(self, dir: Path, n):
        self._mkdir(dir)

        for name in self._get_names(n):
            self._mkdir(dir/name)

    def _build_dir(self, base_dir: Path, expression):
        next_open = expression.index("(") if "(" in expression else len(expression)

        self._build_any(self._mkdir(base_dir/expression[:next_open].strip()), expression[next_open:])

    def _build_print(self, base_dir: Path, expression):
        names = self._get_names(2)

        self._mkdirn(base_dir/names[0], 4)

        self._build_any(self._mkdir(base_dir/names[1]), expression)

    def _build_literal(self, base_dir: Path, expression):
        names = self._get_names(3)

        self._mkdirn(base_dir/names[0], 5)

        type, expression = self._parse_next_word(expression)
        if type == "string":
            self._mkdirn(base_dir/names[1], 2)

            self._mkdir(base_dir/names[2])
            names_2 = self._get_names(len(expression))
            for i, c in enumerate(expression):
                self._mkdir(base_dir/names[2]/names_2[i])
                binary = "{0:08b}".format(ord(c))

                for j, bs in enumerate([binary[:4], binary[4:]]):
                    self._mkdir(base_dir/names[2]/names_2[i]/j)

                    for k, b in enumerate(bs):
                        self._mkdir(base_dir/names[2]/names_2[i]/j/k)

                        if b == "1":
                            self._mkdir(base_dir/names[2]/names_2[i]/j/k/0)
        else:
            raise Exception(f"Unimplemented literal type `{type}`.")
