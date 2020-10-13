class Pessoa:
    #
    def __init__(self, nome=None, idade=35):
        """
        metodo construtor (primeiro a rodar)

        :param nome:
        """
        # atributos
        self.nome = nome
        self.idade = idade
        
    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())