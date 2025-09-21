import sys
import os
import pytest
import pandas as pd
import matplotlib
matplotlib.use("Agg")  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import main  


def test_custos_existem():
    """
    Verifica se o dicionário de custos possui categorias esperadas
    """
    custos = main.custos
    assert "Alimentação" in custos
    assert "Moradia (parcela da criança: água, luz, internet, aluguel)" in custos
    assert isinstance(custos["Saúde (consultas/medicamentos)"], (int, float))

def test_dataframe_total():
    """
    Testa se o DataFrame possui o total correto
    """
    df = main.df
    total_linha = df[df["Categoria"] == "TOTAL"]["Valor (R$)"].iloc[0]
    assert total_linha == sum(main.custos.values())

def test_valor_formatado():
    df = main.df
    exemplo = df[df["Categoria"] == "Alimentação"]["Valor Formatado"].iloc[0]
    assert exemplo.startswith("R$ ")
    assert "," in exemplo  
    
    if int(main.custos["Alimentação"]) >= 1000:
        assert "." in exemplo

def test_dataframe_colunas():
    """
    Verifica se as colunas essenciais existem
    """
    df = main.df
    for col in ["Categoria", "Valor (R$)", "Valor Formatado"]:
        assert col in df.columns

def test_grafico_gera_sem_erros():
    """
    Testa se o gráfico pode ser gerado sem exceção
    """
    try:
        fig = main.plt.figure()
        ax = fig.add_subplot(111)
        ax.bar(main.df_plot["Categoria"], main.df_plot["Valor (R$)"])
    except Exception as e:
        pytest.fail(f"Erro ao gerar gráfico: {e}")
