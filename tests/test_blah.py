from construdelas.tutorias.classes import Turma, FaixaDeHorario, Materia, Professor, HorarioDoProfessor, DiaDaSemana


def test_professor_deve_ter_2_turmas():
    sexto_ano_a = Turma(
        nome="sexto ano A",
        aulas={
            FaixaDeHorario("07:00-08:00"): Materia("Português"),
            FaixaDeHorario("08:00-09:00"): Materia("Matemática"),
            FaixaDeHorario("11:00-12:00"): Materia("Matemática"),
        },
    )

    sexto_ano_b = Turma(
        nome="sexto ano B",
        aulas={
            FaixaDeHorario("07:00-08:00"): Materia("Matemática"),
            FaixaDeHorario("08:00-09:00"): Materia("Biologia"),
            FaixaDeHorario("11:00-12:00"): Materia("Historia"),
        },
    )
    professor_a = Professor(
        disciplinas=[Materia("Matemática"), Materia("Geometria")],
        horarios=[HorarioDoProfessor(DiaDaSemana("segunda"), FaixaDeHorario("07:00-08:00"), sexto_ano_a),
                  HorarioDoProfessor(DiaDaSemana("segunda"), FaixaDeHorario("08:00-09:00"), sexto_ano_b),
                  HorarioDoProfessor(DiaDaSemana("segunda"), FaixaDeHorario("10:00-11:00"), sexto_ano_a)]
    )

    assert professor_a.quantidade_de_turmas == 2
