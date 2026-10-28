# testes/ — Testes

Testes das fórmulas e das regras de negócio. Cada requisito da matriz de rastreabilidade (`docs/relatorio_oa2.md`, seção 10) deve ter pelo menos um teste.

Casos de referência (dados do enunciado), com resultado esperado:

| Teste | Entrada | Esperado |
| --- | --- | --- |
| Atendimento da meta | produção 1.420, meta 1.500 | 94,7% (amarelo) |
| Índice de defeitos | 60 reprovados em 1.420 | 4,2% (amarelo) |
| Produtividade | 1.420 em turno de 480 min com 85 min de parada | 215,7 unid/h |
| Integridade | aprovados + reprovados ≠ realizada | registro recusado |
| Meta duplicada | mesma data, turno e produto | registro recusado (RN09) |
| Importação com erro | planilha com 1 linha inválida | nada gravado (RN06) |

Ferramenta de testes: a definir pela equipe.
