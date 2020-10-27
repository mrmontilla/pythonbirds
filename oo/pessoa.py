class Pessoa:
    """

    """

    # Definindo atributos
    # Aceita variaveis de inicialização, com valor padrão
    def __init__(self, s_nome=None, idade=35):
        self.nome = s_nome
        self.idade = idade

    # Definição de metodo
    def cumprimentar(self):
        """

        """
        return f'Olá {id(self)}'



# executa se chamado diretamente
if __name__ == '__main__':
    # Construindo o metodo
    p = Pessoa()

    # Chamando o metodo
    print(Pessoa.cumprimentar(p))

    #chamando o metodo corretamente
    print(id(p))
    print(p.cumprimentar())

    # Chamada de atributo
    print(p.nome)

    # alterar valor de atributo
    p.nome = 'Joca'
    print(p.nome)

    # Construindo o metodo, com passagem de parametros
    p = Pessoa("Lucia")
    print(p.nome)
    print(p.idade)
