"""Exercício Prático 5 - Auditoria simbólica de regras sob concept drift."""

from __future__ import annotations

from typing import Callable, Dict, List

Case = Dict[str, int]


def regra_antiga(caso: Case) -> int:
    # Regra originalmente válida: classificar como RISCO_ALTO se
    # TEMPERATURE_HIGH e VIBRATION_HIGH forem verdadeiros.
    return int(caso.get("TEMPERATURE_HIGH", 0) and caso.get("VIBRATION_HIGH", 0))


CASOS_ANTIGOS: List[Case] = [
    {"TEMPERATURE_HIGH": 1, "VIBRATION_HIGH": 1, "esperado": 1},
    {"TEMPERATURE_HIGH": 1, "VIBRATION_HIGH": 0, "esperado": 0},
    {"TEMPERATURE_HIGH": 0, "VIBRATION_HIGH": 1, "esperado": 0},
]

CASOS_NOVOS: List[Case] = [
    {"TEMPERATURE_HIGH": 1, "VIBRATION_HIGH": 1, "ALARM_ON": 0, "esperado": 0},
    {"TEMPERATURE_HIGH": 1, "VIBRATION_HIGH": 1, "ALARM_ON": 1, "esperado": 1},
    {"TEMPERATURE_HIGH": 1, "VIBRATION_HIGH": 0, "ALARM_ON": 1, "esperado": 0},
    {"TEMPERATURE_HIGH": 0, "VIBRATION_HIGH": 1, "ALARM_ON": 1, "esperado": 0},
]


def auditar(nome: str, casos: List[Case], regra: Callable[[Case], int]) -> None:
    print(f"\n=== Auditoria em {nome} ===")
    acertos = 0
    for i, caso in enumerate(casos, start=1):
        previsto = regra(caso)
        esperado = caso["esperado"]
        status = "OK" if previsto == esperado else "FALHA"
        print(
            f"Caso {i}: previsto={previsto} | esperado={esperado} | status={status} | dados={caso}"
        )
        acertos += int(previsto == esperado)

    taxa = 100 * acertos / len(casos)
    print(f"Taxa de acerto da regra: {taxa:.1f}%")
    if taxa < 100:
        print("Conclusão: a regra precisa ser revisada, pois o ambiente mudou.")
    else:
        print("Conclusão: a regra continua aderente ao ambiente avaliado.")


def main() -> None:
    print("Exercício Prático 5 - Auditoria simbólica de concept drift")
    print("A regra antiga é testada em dados antigos e em novos dados.\n")
    auditar("dados antigos", CASOS_ANTIGOS, regra_antiga)
    auditar("dados novos", CASOS_NOVOS, regra_antiga)

    print("\nSugestão de revisão:")
    print(
        "Uma possível atualização seria exigir também ALARM_ON=1 nos novos casos, "
        "mostrando que mudanças no ambiente podem tornar a regra original insuficiente."
    )


if __name__ == "__main__":
    main()
