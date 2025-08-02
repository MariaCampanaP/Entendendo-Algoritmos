def pesquisa_binaria(lista, item):
    # => Baixo e alto acompanham a parte da lista que você está procurando.
    baixo = 0 
    alto = len(lista) - 1

    while baixo <= alto: # => enquanto ainda não conseguiu chegar a um único elemento...
        meio = (baixo + alto) // 2 # => ...verifica o elemento central.
        chute = lista[meio]
        if chute == item: # => Acha o item.
            return meio
        if chute > item: # => O chute foi muito alto.
            alto = meio - 1
        else: # => O chute foi muito baixo.
            baixo = meio + 1
    return None # => O item não existe.

minha_lista = [1, 3, 5, 7, 9] # => Vamos testá-lo.

# => Lembre-se, as listas começam no 0. O próximo endereço tem índice 1.
print (pesquisa_binaria(minha_lista, 3)) # => 1

# => "None" significa nulo em Python. Ele indica que o item não foi encontrado.
print (pesquisa_binaria(minha_lista, -1)) # => None