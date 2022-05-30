import pandas as pd


activities_df = pd.read_excel("activities.xltx")

assessores_df = pd.read_excel("assessores.xltx")

captacao_liq_df = pd.read_excel("captacao_liq.xltx")

diversificacao_df = pd.read_excel("diversificacao.xltx")

leads_df = pd.read_excel("leads.xltx")

transf_entrada_df = pd.read_excel("transf_entrada.xltx")

transf_saida_df = pd.read_excel("transf_saida.xltx")

for i in captacao_liq_df['adv_id']
    captacao_acessor = captacao_liq_df.loc[captacao_liq_df['adv_id'] == i]



