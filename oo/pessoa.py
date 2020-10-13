class Pessoa:
    #
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
