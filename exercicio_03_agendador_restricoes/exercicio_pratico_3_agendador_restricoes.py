"""Exercício Prático 3 - Satisfação de restrições em agenda."""

from __future__ import annotations

HORARIOS = ["H1", "H2", "H3", "H4"]

DISPONIBILIDADE_RECURSO_A = {"H1": 0, "H2": 1, "H3": 1, "H4": 1}
DISPONIBILIDADE_RECURSO_B = {"H1": 1, "H2": 1, "H3": 0, "H4": 1}


def horario_valido(horario: str) -> tuple[bool, list[str]]:
    justificativas: list[str] = []

    # Regra 1: a tarefa principal não pode ocorrer em H2.
    if horario == "H2":
        justificativas.append("Regra 1 violada: H2 é proibido.")

    # Regra 2: se ocorrer em H1, o recurso A deve estar disponível.
    if horario == "H1" and not DISPONIBILIDADE_RECURSO_A[horario]:
        justificativas.append("Regra 2 violada: recurso A indisponível em H1.")

    # Regra 3: a tarefa requer recurso B disponível em qualquer horário.
    if not DISPONIBILIDADE_RECURSO_B[horario]:
        justificativas.append("Regra 3 violada: recurso B indisponível.")

    # Regra 4: H4 é permitido apenas se A e B estiverem disponíveis simultaneamente.
    if horario == "H4" and not (
        DISPONIBILIDADE_RECURSO_A[horario] and DISPONIBILIDADE_RECURSO_B[horario]
    ):
        justificativas.append("Regra 4 violada: H4 requer A e B simultaneamente.")

    return len(justificativas) == 0, justificativas


def main() -> None:
    print("Exercício Prático 3 - Agendador com restrições simbólicas\n")
    solucoes_validas: list[str] = []

    for horario in HORARIOS:
        valido, justificativas = horario_valido(horario)
        print(f"Analisando {horario}...")
        if valido:
            print("  -> horário válido")
            solucoes_validas.append(horario)
        else:
            print("  -> horário inválido")
            for item in justificativas:
                print(f"     * {item}")

    print("\nSoluções finais:")
    if solucoes_validas:
        for horario in solucoes_validas:
            print(f"  - {horario}")
    else:
        print("  Nenhuma solução encontrada.")


if __name__ == "__main__":
    main()
