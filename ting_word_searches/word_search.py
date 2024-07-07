def exists_word(word, instance):
    word = word.lower()
    data = []

    for n in instance._data:
        name = n["nome_do_arquivo"]
        amount_of_word = []

        with open(name, "r") as file:
            for lines, line in enumerate(file, 1):
                if word in line.lower():
                    amount_of_word.append({"linha": lines})

        if amount_of_word:
            data.append(
                {
                    "palavra": word,
                    "arquivo": name,
                    "ocorrencias": amount_of_word,
                }
            )

    return data


def search_by_word(word, instance):
    word = word.lower()
    data = []

    for n in instance._data:
        name = n["nome_do_arquivo"]
        amount_of_word = []

        with open(name, "r") as file:
            for lines, line in enumerate(file, 1):
                if word in line.lower():
                    amount_of_word.append(
                        {"linha": lines, "conteudo": line.strip()}
                    )

        if amount_of_word:
            data.append(
                {
                    "palavra": word,
                    "arquivo": name,
                    "ocorrencias": amount_of_word,
                }
            )

    return data
