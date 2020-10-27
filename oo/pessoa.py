class Pessoa:
    """

    """
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


