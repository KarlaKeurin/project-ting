import os.path as os
import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return
    elif not os.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return

    with open(path_file, "r") as file:
        return file.read().split("\n")
