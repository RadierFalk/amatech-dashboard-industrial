"""T07 Importação de planilhas (RF16, RN06). Supervisor. Tudo ou nada: uma linha inválida recusa o arquivo."""
import pandas as pd
import streamlit as st

from pages.comum import data_hora_br, exigir, mostrar_erro, tabela
from servicos.erros import ErroValidacao
from servicos.historico import ServicoHistorico
from servicos.importador_csv import MODELOS, ImportadorCSV

usuario = exigir("importacao")
st.title("Importação de planilhas")

importador = ImportadorCSV()

st.subheader("1. Tipo de dado")
tipo = st.radio("Tipo de dado", list(MODELOS), format_func=lambda t: MODELOS[t]["titulo"], horizontal=True,
                label_visibility="collapsed")

st.subheader("2. Modelo")
st.download_button(f"Baixar modelo CSV de {MODELOS[tipo]['titulo'].lower()}", importador.modelo_csv(tipo),
                   file_name=f"modelo_{tipo}.csv", mime="text/csv")
opcionais = MODELOS[tipo]["opcionais"]
st.caption("Separador ponto e vírgula. Datas em DD/MM/AAAA e horários em DD/MM/AAAA HH:MM. "
           + (f"Colunas opcionais: {', '.join(opcionais)}." if opcionais else "Todas as colunas são obrigatórias.")
           + (" Importe a produção antes dos defeitos." if tipo == "defeito" else ""))

st.subheader("3. Arquivo")
arquivo = st.file_uploader("Arquivo CSV", type=["csv"], key=f"arquivo_{tipo}")

if arquivo is not None:
    conteudo = arquivo.getvalue()
    st.subheader("4. Prévia das primeiras linhas")
    try:
        previa = importador.ler_arquivo(conteudo)
        st.dataframe(previa.head(10), hide_index=True, width="stretch")
        st.caption(f"{len(previa)} linha(s) no arquivo.")
    except ErroValidacao as erro:
        mostrar_erro(erro)

    if st.button("Importar", type="primary"):
        resultado = importador.importar(conteudo, tipo, usuario.id, arquivo.name)
        st.subheader("5. Resultado")
        if resultado.aceita:
            st.success(f"Arquivo importado: {resultado.importadas} linha(s) gravada(s).")
        else:
            st.error(f"Arquivo recusado: {resultado.rejeitadas} linha(s) com erro. Nada foi gravado. "
                     "Corrija e envie de novo.")
            erros = pd.DataFrame(resultado.erros, columns=["Linha", "Coluna", "Problema"]).fillna("—")
            st.dataframe(erros, hide_index=True, width="stretch")

st.subheader("Histórico de importações")
linhas = ServicoHistorico().importacoes()
for l in linhas:
    l["data_hora"] = data_hora_br(l["data_hora"])
    l["tipo_dado"] = MODELOS[l["tipo_dado"]]["titulo"]
    l["status"] = "Concluída" if l["status"] == "concluida" else "Rejeitada"
tabela(linhas, {"data_hora": "Data e hora", "nome_arquivo": "Arquivo", "tipo_dado": "Tipo", "usuario": "Usuário",
                "linhas_lidas": "Linhas", "linhas_importadas": "Importadas", "status": "Situação"},
       vazio="Nenhuma importação ainda.")
