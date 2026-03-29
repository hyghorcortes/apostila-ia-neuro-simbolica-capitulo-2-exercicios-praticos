"""Exercício Prático 4 - Sistema especialista simples para manutenção.

O foco deste exemplo é a explicação da decisão.
"""

from __future__ import annotations

from typing import Dict, List, Tuple

Case = Dict[str, int]

CASOS = {
    "Equipamento_A": {
        "TEMPERATURE_HIGH": 1,
        "VIBRATION_HIGH": 1,
        "ALARM_ON": 1,
        "RECENT_FAILURE": 0,
    },
    "Equipamento_B": {
        "TEMPERATURE_HIGH": 1,
        "VIBRATION_HIGH": 0,
        "ALARM_ON": 0,
        "RECENT_FAILURE": 0,
    },
    "Equipamento_C": {
        "TEMPERATURE_HIGH": 0,
        "VIBRATION_HIGH": 1,
        "ALARM_ON": 1,
        "RECENT_FAILURE": 1,
    },
}


def inferir(fatos: Case) -> Tuple[str, List[str]]:
    trilha: List[str] = []

    if fatos.get("TEMPERATURE_HIGH", 0) and fatos.get("VIBRATION_HIGH", 0):
        trilha.append(
            "Regra R1 ativada: TEMPERATURE_HIGH AND VIBRATION_HIGH -> INSPECTION_RECOMMENDED"
        )

    if fatos.get("ALARM_ON", 0) and fatos.get("RECENT_FAILURE", 0):
        trilha.append(
            "Regra R2 ativada: ALARM_ON AND RECENT_FAILURE -> MAINTENANCE_URGENT"
        )
        return "MAINTENANCE_URGENT", trilha

    if fatos.get("TEMPERATURE_HIGH", 0) and fatos.get("VIBRATION_HIGH", 0) and fatos.get("ALARM_ON", 0):
        trilha.append(
            "Regra R3 ativada: TEMPERATURE_HIGH AND VIBRATION_HIGH AND ALARM_ON -> MAINTENANCE_URGENT"
        )
        return "MAINTENANCE_URGENT", trilha

    if fatos.get("TEMPERATURE_HIGH", 0) and fatos.get("VIBRATION_HIGH", 0):
        return "INSPECTION_RECOMMENDED", trilha

    trilha.append("Nenhuma regra crítica ativada -> NORMAL_OPERATION")
    return "NORMAL_OPERATION", trilha


def main() -> None:
    print("Exercício Prático 4 - Sistema especialista de manutenção\n")
    for nome, fatos in CASOS.items():
        print(f"=== {nome} ===")
        for chave, valor in fatos.items():
            print(f"{chave} = {valor}")
        conclusao, trilha = inferir(fatos)
        print("Conclusão:", conclusao)
        print("Explicação:")
        for passo in trilha:
            print(" -", passo)
        print()


if __name__ == "__main__":
    main()
