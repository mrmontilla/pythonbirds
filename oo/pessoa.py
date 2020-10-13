class Pessoa:
    # Atributo de classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        """
        metodo construtor (primeiro a rodar)

        :param *filhos:
        :param nome:
        """
        # atributos
        self.nome = nome
        self.idade = idade
        self.filhos = filhos

    def cumprimentar(self) -> object:
        return 'Olá'

if __name__ == '__main__':
    marcelo = Pessoa(nome='marcelo')
    luciano = Pessoa(marcelo, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    # print(luciano.sobrenome) # dara erro
    #criando atributos dinamicamente
    luciano.sobrenome = 'silva'
    print(luciano.sobrenome)

    # atributos dos objetos
    print(luciano.__dict__)
    print(marcelo.__dict__)

    # removendo atributos
    del luciano.filhos
    # atributos dos objetos
    print(luciano.__dict__)
    print(marcelo.__dict__)

    # atributo de classe
    print(luciano.idade)

    #modifica atributo objeto
    luciano.olhos = 1
    print(luciano.olhos)
    print(marcelo.olhos)
