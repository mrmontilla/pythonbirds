class Pessoa:
    """

    """

    # Definindo atributos
    # Atributos de classe
    olhos = 2





    # Aceita variaveis de inicialização, com valor padrão
    def __init__(self, *filhos, s_nome=None, idade=35):
        self.filhos = list(filhos)
        self.nome = s_nome
        self.idade = idade

    # Definição de metodo
    def cumprimentar(self):
        """

        """
        return f'Olá {id(self)}'

    # Metodos estaticos
    @staticmethod  # decorator
    def metodo_estatico():
       return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'




# executa se chamado diretamente


if __name__ == '__main__':
    # Construindo o metodo
    maria = Pessoa(s_nome='Maria')
    luciano = Pessoa(maria, s_nome='Luciano')

    # Chamando o metodo
    print(Pessoa.cumprimentar(luciano))

    # chamando o metodo corretamente
    print(id(luciano))
    print(luciano.cumprimentar())

    # Chamada de atributo
    # print(luciano.nome)

    # alterar valor de atributo
    # luciano.nome = 'Joca'
    # print(luciano.nome)

    # Construindo o metodo, com passagem de parametros
    # luciano = Pessoa("Lucia")
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    # criando atributos
    luciano.sobrenome = 'Silva'
    print(luciano.sobrenome)

    # verificando atributos de instancia
    print(luciano.__dict__)
    print(maria.__dict__)
    print()

    # removendo atributos de instancia
    del luciano.filhos
    del maria.idade
    print(luciano.__dict__)
    print(maria.__dict__)

    # atributos de classe
    print(Pessoa.olhos)
    print(luciano.olhos)
    print()
    print(id(Pessoa.olhos))
    print(id(luciano.olhos))
    print(id(maria.olhos))

    luciano.olhos = 1
    print(luciano.__dict__)
    print(maria.__dict__)

    print()
    print(Pessoa.metodo_estatico())
    print(luciano.metodo_estatico())
    print(maria.metodo_estatico())

    print()
    print(Pessoa.nome_e_atributo_de_classe())
    print(luciano.nome_e_atributo_de_classe())
    print(maria.nome_e_atributo_de_classe())
