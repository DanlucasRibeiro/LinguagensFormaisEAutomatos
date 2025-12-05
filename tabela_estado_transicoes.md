| **Estado Atual**      | **Entrada do Usuário**                                  | **Próximo Estado** | **Ação do Sistema**      |
| --------------------- | ------------------------------------------------------- | ------------------ | ------------------------ |
| **SAUDACAO**          | dizer "quero pedir"                                     | ESCOLHER_PROTEINA  | Pede para iniciar pedido |
| **ESCOLHER_SABOR**    | sabor válido (cheeseburger, frango, veggie, x-salada)   | ESCOLHER_TAMANHO   | Pergunta qual carne      |
| **ESCOLHER_TAMANHO**  | tamanho válido (pequena, média, media, grande)          | ESCOLHER_BEBIDA    | Pergunta tamanho         |
| **INFORMAR_ENDERECO** | texto com mais de 5 caracteres                          | CONFIRMAR          | Mostra resumo            |
| **CONFIRMAR**         | "confirmar"                                             | PAGAMENTO          | Pergunta pagamento       |
| **PAGAMENTO**         | "dinheiro", "cartão"                                    | FINALIZADO         | Finaliza pedido          |
| **FINALIZADO**        | —                                                       | —                  | Mostra pedido e encerra  |
| **CANCELADO**         | —                                                       | FINALIZADO         | Cancela e encerra        |
