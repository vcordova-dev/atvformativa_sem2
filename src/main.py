import pandas as pd
import matplotlib.pyplot as plt

custos = {
    "Alimentação": 500,
    "Educação (escola/material/transporte)": 500,
    "Saúde (consultas/medicamentos)": 150,
    "Roupas/Calçados": 200,
    "Lazer/Atividades": 200,
    "Moradia (parcela da criança: água, luz, internet, aluguel)": 300
}

df = pd.DataFrame([{"Categoria": k, "Valor (R$)": v} for k, v in custos.items()])

total = pd.DataFrame([{"Categoria": "TOTAL", "Valor (R$)": df["Valor (R$)"].sum()}])
df = pd.concat([df, total], ignore_index=True)

df["Valor Formatado"] = df["Valor (R$)"].apply(
    lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)


print(df[["Categoria", "Valor Formatado"]].to_string(index=False))

df_plot = df[df["Categoria"] != "TOTAL"].copy()
valores = df_plot["Valor (R$)"]
categorias = df_plot["Categoria"]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


ax1.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=90, colors=plt.cm.get_cmap("tab20").colors)
ax1.set_title("Distribuição dos Custos (Pizza)", fontsize=14)


bars = ax2.bar(categorias, valores, color=plt.cm.get_cmap("tab20").colors)
ax2.set_title("Custos Mensais por Categoria", fontsize=14)
ax2.set_ylabel("Valor (R$)")
ax2.tick_params(axis="x", rotation=30)


for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, height + 10, f"R$ {height:,.0f}".replace(",", "X").replace(".", ",").replace("X", "."), 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
