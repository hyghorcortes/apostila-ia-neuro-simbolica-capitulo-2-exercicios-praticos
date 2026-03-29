"""Exercício Prático 1 - Base de conhecimento para classificação simbólica de frutas.

Este script demonstra como representar fatos e regras simbólicas simples
em Python, sem bibliotecas externas.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List

FactSet = Dict[str, int]


@dataclass
class Rule:
    nome: str
    conclusao: str
    condicao: Callable[[FactSet], bool]
    predicados_relevantes: List[str]

    def avaliar(self, fatos: FactSet) -> bool:
        return self.condicao(fatos)


RULES = [
    Rule(
        nome="Regra_Laranja",
        conclusao="LARANJA",
        condicao=lambda f: f.get("ROUND", 0)
        and f.get("ORANGECOLOR", 0)
        and f.get("FRUIT", 0)
        and f.get("HASSTEM", 0),
        predicados_relevantes=["ROUND", "ORANGECOLOR", "FRUIT", "HASSTEM"],
    ),
    Rule(
        nome="Regra_Maca",
        conclusao="MACA",
        condicao=lambda f: f.get("ROUND", 0)
        and f.get("REDORGREEN", 0)
        and f.get("FRUIT", 0)
        and f.get("HASSTEM", 0),
        predicados_relevantes=["ROUND", "REDORGREEN", "FRUIT", "HASSTEM"],
    ),
    Rule(
        nome="Regra_Banana",
        conclusao="BANANA",
        condicao=lambda f: f.get("LONGSHAPE", 0)
        and f.get("YELLOW", 0)
        and f.get("FRUIT", 0)
        and f.get("PEEL", 0),
        predicados_relevantes=["LONGSHAPE", "YELLOW", "FRUIT", "PEEL"],
    ),
]


OBJETOS = {
    "objeto_1": {"ROUND": 1, "ORANGECOLOR": 1, "FRUIT": 1, "HASSTEM": 1},
    "objeto_2": {"ROUND": 1, "REDORGREEN": 1, "FRUIT": 1, "HASSTEM": 1},
    "objeto_3": {"LONGSHAPE": 1, "YELLOW": 1, "FRUIT": 1, "PEEL": 1},
    "objeto_4": {"ROUND": 1, "YELLOW": 1, "FRUIT": 1},
}


def classificar_objeto(nome_objeto: str, fatos: FactSet) -> str:
    print(f"\n=== Avaliando {nome_objeto} ===")
    print("Fatos observados:")
    for chave, valor in sorted(fatos.items()):
        print(f"  - {chave} = {valor}")

    conclusoes: List[str] = []

    for regra in RULES:
        satisfeita = regra.avaliar(fatos)
        detalhes = ", ".join(f"{p}={fatos.get(p, 0)}" for p in regra.predicados_relevantes)
        print(f"\n{regra.nome}: {detalhes}")
        print(f"Resultado da regra: {'VERDADEIRO' if satisfeita else 'FALSO'}")
        if satisfeita:
            conclusoes.append(regra.conclusao)

    if len(conclusoes) == 1:
        resultado = conclusoes[0]
    elif len(conclusoes) > 1:
        resultado = f"AMBIGUO ({', '.join(conclusoes)})"
    else:
        resultado = "DESCONHECIDO"

    print(f"\nClassificação final: {resultado}")
    return resultado


def main() -> None:
    print("Exercício Prático 1 - Classificação simbólica de frutas")
    print("Este exemplo usa apenas fatos binários e regras explícitas.\n")
    for nome_objeto, fatos in OBJETOS.items():
        classificar_objeto(nome_objeto, fatos)


if __name__ == "__main__":
    main()
