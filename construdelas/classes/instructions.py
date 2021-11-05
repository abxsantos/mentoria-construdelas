"""
Classes são utilizadas para criar estruturas definidas.

Estas, definem funções chamadas de métodos.

Os mtodos identificam os comportamentos e ações que um
    objeto criado a partir da classe pode executar com
    seus dados.

Uma classe é uma base de como algo deve ser definido.

Enquanto a classe é uma base, uma instância é um objeto que é
    construído a partir de uma classe e contém dados reais.
"""

# Definindo classes
import random
from typing import List


class Carta:

    def __init__(self, naipe="♦", valor="10"):
        """
        As propriedades que os objetos ``Carta`` devem possuir, são definidos neste método.

        Toda vez que uma ``Carta`` é criada, o método ``__init__`` irá definir o estado do
            objeto, atribuindo os valores as propriedades.

        Ou seja, ``__ init __`` inicializa cada nova instância da classe.
        """
        """
        Neste exemplo a classe ``Carta`` possui a propriedade ``naipe`` (♣, v, ♥, ♠),
        e a propriedade valor (2,3,4,5,6,7,8,9,10,K,Q,J,A).
        """
        self.naipe = naipe
        self.valor = valor


# Instanciando um objeto ``Carta`` simulando um dois de ouros.
dois_de_paus = Carta(naipe="♣", valor="2")
print()


dois_de_ouros = Carta(naipe="♦", valor="2")

print(dois_de_ouros.naipe)
print(dois_de_ouros.valor)
print(type(dois_de_ouros))

# Instanciando um novo objeto ``Carta`` simulando um 5 de espadas.
cinco_de_espadas = Carta(naipe="♠", valor="5")

print(cinco_de_espadas.naipe)
print(cinco_de_espadas.valor)
print(type(cinco_de_espadas))

# Objetos criados podem ser comparados
print(dois_de_ouros == cinco_de_espadas)


class Carta:
    """
    Classes podem ter atributos associados a classe, como ``tipo``
    """
    tipo: str = "cartolina"

    def __init__(self, naipe: str, valor: str) -> None:
        """
        E tributos de instância, como ``naipe`` e ``valor``.
        """
        self.naipe: str = naipe
        self.valor: str = valor


dez_de_paus = Carta(naipe="♣", valor="10")
print(dez_de_paus.naipe)
print(dez_de_paus.valor)
print(dez_de_paus.tipo)
print(type(dez_de_paus))

"""
Uma das maiores vantagens de usar classes para organizar dados é que
    as instâncias têm a garantia de ter os atributos que você espera.

Todas as instâncias de ``Carta`` têm atributos ``naipe``, ``valor`` e
    ``tipo``, então você pode usar esses atributos com confiança, sabendo
    que eles sempre retornarão um valor.
"""

"""
Os métodos de instância são funções definidas dentro de uma classe e só
    podem ser chamados a partir de uma instância dessa classe.

Assim como ``__ init __``, o primeiro parâmetro de um método de instância
    é sempre ``self``.
"""


class Baralho:

    def __init__(self, cartas: List[Carta] = None) -> None:
        self.cartas: List[Carta] = cartas or []

    def embaralhar(self) -> None:
        random.shuffle(self.cartas)

    def tirar_do_topo(self) -> Carta:
        return self.cartas.pop(0)

    def tirar_de_baixo(self) -> Carta:
        return self.cartas.pop(-1)

    @property
    def numero_de_cartas(self):
        return len(self.cartas)

    def cortar_no_meio(self):
        if self.numero_de_cartas % 2:
            meio = self.numero_de_cartas // 2
            primeira_metade = self.cartas[:meio]
            segunda_metade = self.cartas[:meio]
            return Baralho(cartas=primeira_metade), Baralho(cartas=segunda_metade)

cinco_de_espadas = Carta(naipe="♠", valor="5")
dois_de_ouros = Carta(naipe="♦", valor="2")
dez_de_paus = Carta(naipe="♣", valor="10")
cartas_do_baralho = [cinco_de_espadas, dois_de_ouros, dez_de_paus]
baralho = Baralho(cartas=cartas_do_baralho)

print(baralho.cartas)

baralho.embaralhar()
print(baralho.cartas)
#
carta_de_baixo = baralho.tirar_de_baixo()
print(f"A carta de baixo é <Carta valor: {carta_de_baixo.valor}, naipe: {carta_de_baixo.naipe}>")
print(f"O baralho agora tem {baralho.numero_de_cartas} cartas")



carta_do_topo = baralho.tirar_do_topo()
print(f"A carta do topo é <Carta valor: {carta_do_topo.valor}, naipe: {carta_do_topo.naipe}>")
print(f"O baralho agora tem {baralho.numero_de_cartas} cartas")


class FileParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_file(self):
        print(f"Deve ler o arquivo do caminho: {self.file_path}")


class CSVParser(FileParser):

    def clean_dot_and_commas(self):
        print(f"Deve remover os ; do arquivo: {self.file_path}")


class JSONParser(FileParser):

    def replace_quotes(self):
        print(f"Deve trocar as aspas duplas por aspas simples do arquivo: {self.file_path}")


file_parser = FileParser(file_path="arquivo.txt")
file_parser.read_file()

csv_parser = CSVParser(file_path="arquivo.txt")
csv_parser.read_file()
csv_parser.clean_dot_and_commas()

json_parser = JSONParser(file_path="arquivo.txt")
json_parser.read_file()
json_parser.replace_quotes()
