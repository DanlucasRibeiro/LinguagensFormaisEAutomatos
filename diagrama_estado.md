# 2 Diagrama de Estados (Mermaid)

```mermaid
stateDiagram-v2
    direction TB

    [*] --> SAUDACAO

    SAUDACAO --> ESCOLHER_PROTEINA: "quero pedir"

    ESCOLHER_PROTEINA --> ESCOLHER_PAO: "Tipo escolhido"
    ESCOLHER_PAO --> ESCOLHER_TAMANHO: "Pao escolhido"
    ESCOLHER_TAMANHO --> ADICIONAR_EXTRA: "Tamanho escolhido"
    ADICIONAR_EXTRA --> INFORMAR_ENDERECO: "Extra adicionado"
    INFORMAR_ENDERECO --> CONFIRMAR: "Endereco informado"
    CONFIRMAR --> PAGAMENTO: "Pagamento realizado"
    PAGAMENTO --> FINALIZADO: "Preparando pedido"

    CONFIRMAR --> FINALIZADO: "Cancelar"
    CONFIRMAR --> ESCOLHER_PROTEINA: "Alterar"

    FINALIZADO --> [*]
    
    