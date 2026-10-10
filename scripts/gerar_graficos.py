from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)


def salvar(fig, nome_arquivo: str):
    caminho = ASSETS / nome_arquivo
    fig.tight_layout()
    fig.savefig(caminho, format="svg", bbox_inches="tight")
    plt.close(fig)


def grafico_cobertura_inicial():
    labels = ["Statements", "Branches", "Functions", "Lines"]
    values = [85.41, 58.82, 100.0, 98.64]
    colors = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6"]

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    bars = ax.bar(labels, values, color=colors, edgecolor="black", linewidth=0.8)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Cobertura (%)")
    ax.set_title("Cobertura inicial do código")
    ax.set_axisbelow(True)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 2,
            f"{value:.2f}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    return fig


def grafico_mutacao_comparativa():
    categorias = ["Mutation score", "Mutantes cobertos", "Mutantes mortos", "Mutantes sobreviventes"]
    inicial = [73.71, 78.11, 154, 44]
    final = [75.59, 80.10, 158, 40]

    x = range(len(categorias))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.bar([i - width / 2 for i in x], inicial, width=width, label="Inicial", color="#EF4444")
    ax.bar([i + width / 2 for i in x], final, width=width, label="Final", color="#22C55E")

    ax.set_title("Comparação inicial x final da análise de mutação")
    ax.set_xticks(list(x))
    ax.set_xticklabels(categorias, rotation=18, ha="right")
    ax.set_ylabel("Valor")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    for i, value in enumerate(inicial):
        ax.text(i - width / 2, value + 1.5, f"{value:.2f}", ha="center", va="bottom", fontsize=8)
    for i, value in enumerate(final):
        ax.text(i + width / 2, value + 1.5, f"{value:.2f}", ha="center", va="bottom", fontsize=8)

    return fig


def grafico_status_mutantes():
    labels = ["Mortos", "Sobreviventes", "Timeout", "Sem cobertura", "Erros"]
    initial = [154, 44, 3, 12, 0]
    final = [158, 40, 3, 12, 0]

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    ax.bar([i - width / 2 for i in x], initial, width=width, label="Inicial", color="#1D4ED8")
    ax.bar([i + width / 2 for i in x], final, width=width, label="Final", color="#0EA5E9")

    ax.set_title("Status dos mutantes antes e depois dos testes melhorados")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel("Quantidade")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    for i, value in enumerate(initial):
        ax.text(i - width / 2, value + 1.7, f"{value}", ha="center", va="bottom", fontsize=8)
    for i, value in enumerate(final):
        ax.text(i + width / 2, value + 1.7, f"{value}", ha="center", va="bottom", fontsize=8)

    return fig


def main():
    salvar(grafico_cobertura_inicial(), "cobertura-inicial.svg")
    salvar(grafico_mutacao_comparativa(), "mutacao-comparativa.svg")
    salvar(grafico_status_mutantes(), "status-mutantes.svg")
    print(f"Arquivos SVG gerados em: {ASSETS}")


if __name__ == "__main__":
    main()
