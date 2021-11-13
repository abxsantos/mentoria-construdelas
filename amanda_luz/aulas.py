from typing import List, NewType, Dict

FaixaDeHorario = NewType("FaixaDeHorario", str)

Materia = NewType("Materia", str)
DiaDaSemana = NewType("DiaDaSemana", str)


class Aula(object):
    pass


class Turma(object):

    def __init__(self, nome: str, aulas: Dict[str, Aula]):
        self.nome = nome
        self.dias_da_semana = {"segunda": [Aula(numero=1, professor=professor_a)], "terça": [Aula()],
                               "quarta": [Aula()]}


class Professor(object):
    def __init__(
            self, disciplinas: List[Materia],
    ) -> None:
        self.disciplinas = disciplinas

    @property
    def quantidade_de_disciplinas(self) -> int:
        return len(self.disciplinas)


prof_a = Professor(disciplinas=[Materia("Portugues")])


def validar_insercao_de_aulas(turma, aula_a_ser_inserida):
    # Uma turma não pode ter um horario ocupado no mesmo dia de semana mais de uma vez
    pass
