from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for n in instance._data:
        if n["nome_do_arquivo"] == path_file:
            return None

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.enqueue(data)

    print(data, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return None

    path_file = instance.search(0)["nome_do_arquivo"]

    instance.dequeue()

    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if position >= len(instance) or position < 0:
        print("Posição inválida", file=sys.stderr)
        return None

    print(instance.search(position), file=sys.stdout)
