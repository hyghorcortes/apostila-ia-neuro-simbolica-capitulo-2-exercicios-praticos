"""Exercício Prático 2 - Recomendação simbólica de filmes por regras."""

from __future__ import annotations

from typing import Dict

FilmFacts = Dict[str, int]

FILMES = {
    "Filme_A": {
        "IS_INTERESTING": 1,
        "IS_ENGAGING": 1,
        "IS_TOO_LONG": 0,
        "AGE_APPROPRIATE": 1,
    },
    "Filme_B": {
        "IS_INTERESTING": 1,
        "IS_ENGAGING": 0,
        "IS_TOO_LONG": 0,
        "AGE_APPROPRIATE": 1,
    },
    "Filme_C": {
        "IS_INTERESTING": 1,
        "IS_ENGAGING": 1,
        "IS_TOO_LONG": 1,
        "AGE_APPROPRIATE": 1,
    },
    "Filme_D": {
        "IS_INTERESTING": 1,
        "IS_ENGAGING": 1,
        "IS_TOO_LONG": 0,
        "AGE_APPROPRIATE": 0,
    },
}


def recomendar(fatos: FilmFacts) -> bool:
    # Regra principal: recomendar se o filme é interessante, envolvente,
    # não é excessivamente longo e é apropriado para a idade.
    return bool(
        fatos.get("IS_INTERESTING", 0)
        and fatos.get("IS_ENGAGING", 0)
        and not fatos.get("IS_TOO_LONG", 0)
        and fatos.get("AGE_APPROPRIATE", 0)
    )


def explicar(nome_filme: str, fatos: FilmFacts) -> None:
    print(f"\n=== {nome_filme} ===")
    for chave, valor in fatos.items():
        print(f"{chave} = {valor}")

    recomendacao = recomendar(fatos)
    print("\nRegra avaliada:")
    print(
        "WATCH = IS_INTERESTING AND IS_ENGAGING "
        "AND (NOT IS_TOO_LONG) AND AGE_APPROPRIATE"
    )
    print(f"Resultado final: {'RECOMENDADO' if recomendacao else 'NAO RECOMENDADO'}")

    if not recomendacao:
        causas = []
        if not fatos.get("IS_INTERESTING", 0):
            causas.append("não é interessante")
        if not fatos.get("IS_ENGAGING", 0):
            causas.append("não é envolvente")
        if fatos.get("IS_TOO_LONG", 0):
            causas.append("é longo demais")
        if not fatos.get("AGE_APPROPRIATE", 0):
            causas.append("não é adequado para a idade")
        print("Motivos da recusa: " + "; ".join(causas))


def main() -> None:
    print("Exercício Prático 2 - Recomendação simbólica de filmes")
    for nome, fatos in FILMES.items():
        explicar(nome, fatos)


if __name__ == "__main__":
    main()
