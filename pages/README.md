# pages/ — Camada 1: Apresentação

Telas do sistema em Streamlit. Cada arquivo `.py` desta pasta vira automaticamente uma tela no menu lateral; o número no início do nome define a ordem. O login fica em `app.py`, na raiz.

| Tela | Arquivo sugerido | Perfis | Requisitos |
| --- | --- | --- | --- |
| T02 Painel de indicadores | `1_Painel.py` | Supervisor, Gestor, Diretoria | RF06–RF12, RF17 |
| T03 Produção e metas | `2_Producao_e_metas.py` | Operador, Supervisor | RF01, RF02 |
| T04 Qualidade | `3_Qualidade.py` | Operador, Inspetor, Supervisor | RF03, RF04 |
| T05 Paradas | `4_Paradas.py` | Manutenção, Supervisor | RF05 |
| T06 Perdas | `5_Perdas.py` | Supervisor | RF15 |
| T07 Importação de planilhas | `6_Importacao.py` | Supervisor | RF16 |
| T08 Histórico | `7_Historico.py` | Supervisor, Gestor, Diretoria | RF13 |
| T09 Cadastros | `8_Cadastros.py` | Administrador (Supervisor: só limites do semáforo) | RF17, RN08 |
| T10 Usuários | `9_Usuarios.py` | Administrador | RF19 |

Regras desta camada: as telas **não calculam indicadores e não acessam o banco**; elas chamam as classes de `servicos/`. Os wireframes estão em `docs/wireframes/`.
