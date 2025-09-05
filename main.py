import pandas as pd
import matplotlib.pyplot as plt # importando a biblioteca

# ---------- Dados ----------
custos = {
    "Alimentação": 500,
    "Educação (escola/material/transporte)": 500,
    "Saúde (consultas/medicamentos)": 150,
    "Roupas/Calçados": 200,
    "Lazer/Atividades": 200,
    "Moradia (parcela da criança: água, luz, internet, aluguel)": 300
}

# ---------- Criar DataFrame ----------
df = pd.DataFrame([
    {"Categoria": k, "Valor (R$)": v} for k, v in custos.items()
])

# Adicionar linha de total
total = pd.DataFrame([{
    "Categoria": "TOTAL",
    "Valor (R$)": df["Valor (R$)"].sum()
}])
df = pd.concat([df, total], ignore_index=True)

# Criar coluna formatada para exibição
df["Valor Formatado"] = df["Valor (R$)"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# ---------- Mostrar tabela no console ----------
print(df[["Categoria", "Valor Formatado"]].to_string(index=False))

# ---------- Preparar dados para gráficos ----------
df_plot = df[df["Categoria"] != "TOTAL"].copy()

# ---------- Gráfico de Pizza ----------
plt.figure(figsize=(6, 6))
plt.pie(
    df_plot["Valor (R$)"],
    labels=df_plot["Categoria"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribuição dos Custos Mensais")
plt.tight_layout()
plt.show()

# ---------- Gráfico de Barras ----------
plt.figure(figsize=(8, 5))
plt.bar(df_plot["Categoria"], df_plot["Valor (R$)"])
plt.title("Custos Mensais por Categoria")
plt.ylabel("Valor (R$)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
