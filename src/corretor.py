import pandas as pd

respostas =pd.read_excel("data/Respostas.xlsx")
gabarito = pd.read_excel("data/Gabarito.xlsx")

print("\nColunas das respostas:")
print(respostas.columns.tolist())

print("\nQuantidade de respostas:", len(respostas))

print("\nRespostas dos alunos:")
print(respostas.head())

print("\nColunas do gabarito:")
print(gabarito.columns.tolist())

print("\nQuantidade de questões no gabarito:", len(gabarito))

print("\nGabarito:")
print(gabarito.head())

print("\nQuantidade de alunos:", respostas["aluno_nome"].nunique())

sem_nome = respostas[
    respostas["aluno_nome"].isna() |
    (respostas["aluno_nome"] == "")
]

print("\nQuantidade de Nome de aluno nulo ou em branco:", len(sem_nome))

print("\nQuantidade de questões respondidas por cada aluno:")
respostas_por_aluno = respostas.groupby("aluno_nome").size()
print(respostas_por_aluno)

print("\nQuestões respondidas por Userl Civico:")

userl = respostas[respostas["aluno_nome"] == "Userl Civico"]

print(userl["num_exercicio"].value_counts().sort_index())

print("\nRespostas duplicadas do Userl Civico:")

print(
    userl.groupby("num_exercicio")["resp_aluno"]
    .agg(list)
)


print("\nQuantidade de respostas NaN por aluno:")

nan_por_aluno = (
    respostas.groupby("aluno_nome")["resp_aluno"]
    .apply(lambda x: x.isna().sum())
)

print(nan_por_aluno)

print("\nAs questões do gabarito são distintas e de 1 a 90?")
print(set(gabarito["Questão"]) == set(range(1, 91)))

print("\nAs questões das respostas dos alunos são distintas e de 1 a 90?")
print(set(respostas["num_exercicio"]) == set(range(1, 91)))

print("\nValores registrados no gabarito:")
print(gabarito["Gabarito"].value_counts(dropna=False))

print("\nValores registrados nas respostas dos alunos:")
print(respostas["resp_aluno"].value_counts(dropna=False))



respostas["resp_aluno_padronizada"] = respostas["resp_aluno"].str.upper()

print("\nColunas das respostas:")
print(respostas.columns)

print("\nColunas do gabarito:")
print(gabarito.columns)

respostas_com_gabarito = respostas.merge(
    gabarito,
    left_on="num_exercicio",
    right_on="Questão",
    how="left"
)

print("\nRespostas dos alunos com o gabarito:")
print(respostas_com_gabarito.head(10).to_string())

import numpy as np

respostas_com_gabarito["resultado"] = np.select(
    [
        respostas_com_gabarito["resp_aluno_padronizada"].isna(),
        respostas_com_gabarito["resp_aluno_padronizada"] == respostas_com_gabarito["Gabarito"]
    ],
    [
        "Sem resposta",
        "Correta"
    ],
    default="Incorreta"
)

print("\nResultado das questões:")
print(
    respostas_com_gabarito[
        [
            "aluno_nome",
            "num_exercicio",
            "resp_aluno_padronizada",
            "Gabarito",
            "resultado"
        ]
    ].head(20).to_string(index=False)
)

print("\nQuantidade de questões por resultado:")
print(respostas_com_gabarito["resultado"].value_counts())

print("\nQuantidade de registros antes do processamento:")
print(len(respostas))

print("\nQuantidade de registros após o merge:")
print(len(respostas_com_gabarito))

respostas_tratadas = respostas_com_gabarito.copy()

respostas_tratadas = respostas_tratadas.sort_values(
    by="resp_aluno_padronizada",
    na_position="last"
)

respostas_tratadas = respostas_tratadas.drop_duplicates(
    subset=["aluno_nome", "num_exercicio"],
    keep="first"
)

resultado_por_aluno = (
    respostas_tratadas
    .groupby(["aluno_nome", "resultado"])
    .size()
    .unstack(fill_value=0)
)

print("\nResultado por aluno:")
print(resultado_por_aluno)

print("\nQuantidade de registros após a ordenação:")
print(len(respostas_tratadas))

print("\nQuantidade de registros por aluno após o tratamento:")

print(
    respostas_tratadas.groupby("aluno_nome").size()
)

resultado_por_aluno = resultado_por_aluno.rename(
    columns={
        "Correta": "total_acertos",
        "Incorreta": "erros",
        "Sem resposta": "sem_resposta"
    }
)

resultado_por_aluno["total_questoes"] = (
    resultado_por_aluno["total_acertos"]
    + resultado_por_aluno["erros"]
    + resultado_por_aluno["sem_resposta"]
)

resultado_por_aluno["percentual_acerto"] = (
    resultado_por_aluno["total_acertos"]
    / resultado_por_aluno["total_questoes"]
    * 100
).round(2)

print("\nDesempenho final por aluno:")
print(resultado_por_aluno)


print("\nQuantidade de alunos:")
print(resultado_por_aluno.index.nunique())

print("\nQuantidade de questões por aluno:")
print(resultado_por_aluno["total_questoes"].value_counts())

media_geral_acertos = resultado_por_aluno["total_acertos"].mean()

media_geral_percentual = (
    media_geral_acertos / 90 * 100
).round(2)

print("\nMédia geral de acertos da turma:")
print(f"Valor absoluto: {media_geral_acertos:.2f} questões")
print(f"Percentual: {media_geral_percentual:.2f}%")

resultado_detalhado = respostas_tratadas[
    [
        "aluno_nome",
        "num_exercicio",
        "resp_aluno_padronizada",
        "Gabarito",
        "resultado"
    ]
].copy()

resultado_detalhado = resultado_detalhado.rename(
    columns={
        "num_exercicio": "questao",
        "resp_aluno_padronizada": "resposta_aluno",
        "Gabarito": "gabarito"
    }
)

print("\nResultado detalhado da correção:")
print(resultado_detalhado.head(20).to_string(index=False))

print("\nQuantidade de registros na correção detalhada:")
print(len(resultado_detalhado))

media_geral_acertos = resultado_por_aluno["total_acertos"].mean()

media_geral_percentual = (
    media_geral_acertos / 90 * 100
).round(2)

print("\nMédia geral de acertos da turma:")
print(f"Valor absoluto: {media_geral_acertos:.2f} questões")
print(f"Percentual: {media_geral_percentual:.2f}%")

resultado_por_aluno = resultado_por_aluno.reset_index()

resultado_detalhado = resultado_detalhado.sort_values(
    by=["aluno_nome", "questao"]
)

print("\nResultado detalhado da correção:")
print(resultado_detalhado.head(20).to_string(index=False))

print("\nTabela final de desempenho por aluno:")
print(resultado_por_aluno.to_string(index=False))

with pd.ExcelWriter("output/resultado_simulado.xlsx", engine="openpyxl") as writer:
    resultado_por_aluno.to_excel(
        writer,
        sheet_name="Desempenho_Alunos",
        index=False
    )

    resultado_detalhado.to_excel(
        writer,
        sheet_name="Correcao_Detalhada",
        index=False
    )

print("\nArquivo output/resultado_simulado.xlsx criado com sucesso!")