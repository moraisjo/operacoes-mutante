from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

plt.style.use("seaborn-v0_8-colorblind")
plt.rcParams.update(
    {
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#FFFFFF",
        "savefig.facecolor": "#FFFFFF",
        "axes.edgecolor": "#2B2B2B",
        "axes.labelcolor": "#1A1A1A",
        "axes.titlecolor": "#1A1A1A",
        "xtick.color": "#1A1A1A",
        "ytick.color": "#1A1A1A",
        "text.color": "#1A1A1A",
        "font.family": ["DejaVu Sans", "Arial", "Liberation Sans", "sans-serif"],
        "font.size": 10.5,
        "axes.titlesize": 14,
        "axes.labelsize": 10.5,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.fontsize": 9.5,
    }
)


def salvar(fig, nome_arquivo: str):
    caminho = ASSETS / nome_arquivo
    fig.tight_layout()
    fig.savefig(caminho, format="svg", bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def grafico_cobertura_inicial():
    labels = ["Statements", "Branches", "Functions", "Lines"]
    values = [85.41, 58.82, 100.0, 98.64]
    colors = ["#0173B2", "#DE8F05", "#029E73", "#575757"]

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    bars = ax.bar(labels, values, color=colors, edgecolor="#2C2C2C", linewidth=1.0)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Cobertura (%)")
    ax.set_title("Cobertura inicial do código")
    ax.set_axisbelow(True)
    ax.grid(axis="y", linestyle="--", linewidth=0.7, alpha=0.45, color="#8A8A8A")

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 2,
            f"{value:.2f}%",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

    return fig


def grafico_mutacao_comparativa():
    categorias = ["Mutation score", "Mutantes cobertos", "Mutantes mortos", "Mutantes sobreviventes"]
    inicial = [73.71, 78.11, 154, 44]
    final = [75.59, 80.10, 158, 40]

    x = range(len(categorias))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.bar(
        [i - width / 2 for i in x],
        inicial,
        width=width,
        label="Inicial",
        color="#0173B2",
        edgecolor="#2C2C2C",
        linewidth=1.0,
        hatch="//",
    )
    ax.bar(
        [i + width / 2 for i in x],
        final,
        width=width,
        label="Final",
        color="#DE8F05",
        edgecolor="#2C2C2C",
        linewidth=1.0,
        hatch="\\\\",
    )

    ax.set_title("Comparação inicial x final da análise de mutação")
    ax.set_xticks(list(x))
    ax.set_xticklabels(categorias, rotation=18, ha="right")
    ax.set_ylabel("Valor")
    ax.set_ylim(0, 180)
    ax.legend(frameon=True, facecolor="#FFFFFF", edgecolor="#C9C9C9")
    ax.grid(axis="y", linestyle="--", linewidth=0.7, alpha=0.45, color="#8A8A8A")

    for i, value in enumerate(inicial):
        label = f"{value:.2f}" if isinstance(value, float) else str(value)
        ax.text(i - width / 2, value + 2.5, label, ha="center", va="bottom", fontsize=8, fontweight="bold")
    for i, value in enumerate(final):
        label = f"{value:.2f}" if isinstance(value, float) else str(value)
        ax.text(i + width / 2, value + 2.5, label, ha="center", va="bottom", fontsize=8, fontweight="bold")

    return fig


def grafico_status_mutantes():
    labels = ["Mortos", "Sobreviventes", "Timeout", "Sem cobertura", "Erros"]
    initial = [154, 44, 3, 12, 0]
    final = [158, 40, 3, 12, 0]

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    ax.bar(
        [i - width / 2 for i in x],
        initial,
        width=width,
        label="Inicial",
        color="#0173B2",
        edgecolor="#2C2C2C",
        linewidth=1.0,
        hatch="//",
    )
    ax.bar(
        [i + width / 2 for i in x],
        final,
        width=width,
        label="Final",
        color="#DE8F05",
        edgecolor="#2C2C2C",
        linewidth=1.0,
        hatch="\\\\",
    )

    ax.set_title("Status dos mutantes antes e depois dos testes melhorados")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel("Quantidade")
    ax.legend(frameon=True, facecolor="#FFFFFF", edgecolor="#C9C9C9")
    ax.grid(axis="y", linestyle="--", linewidth=0.7, alpha=0.45, color="#8A8A8A")

    for i, value in enumerate(initial):
        ax.text(i - width / 2, value + 1.7, f"{value}", ha="center", va="bottom", fontsize=8, fontweight="bold")
    for i, value in enumerate(final):
        ax.text(i + width / 2, value + 1.7, f"{value}", ha="center", va="bottom", fontsize=8, fontweight="bold")

    return fig


def main():
    salvar(grafico_cobertura_inicial(), "cobertura-inicial.svg")
    salvar(grafico_mutacao_comparativa(), "mutacao-comparativa.svg")
    salvar(grafico_status_mutantes(), "status-mutantes.svg")
    print(f"Arquivos SVG gerados em: {ASSETS}")


if __name__ == "__main__":
    main()
