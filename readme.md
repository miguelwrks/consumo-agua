# Programa Consumo Água

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-blue?style=for-the-badge)

Este projeto consiste em um script em Python que analisa e classifica a faixa de consumo mensal de água de um imóvel de acordo com a sua tipologia (Casa, Apartamento ou Comercial).

---

## 💡 Lógica Utilizada

1. **Limpeza do Terminal:** O programa possui uma função `clear()` que verifica o sistema operacional (`os.name`) e executa o comando apropriado (`cls` para Windows ou `clear` para Linux/macOS) para manter o terminal organizado durante a exibição dos resultados.
2. **Entrada de Dados:** Solicita ao usuário o tipo do imóvel (convertido para texto) e o consumo mensal de água em metros cúbicos ($m^3$, convertido para `float`).
3. **Mapeamento de Categoria:** Utiliza a estrutura de controle `match/case` para direcionar a análise conforme o tipo de imóvel informado.
4. **Exibição do Diagnóstico:** Exibe mensagens orientativas baseadas em faixas de consumo específicas para a tipologia selecionada.

---

## 🔀 Estrutura de Decisão (`match` / `case` e `if` / `elif` / `else`)

- **`case 'comercial':`**
  - **Regra:** Exibe mensagem direcionada para tarifa comercial e consulta de plano corporativo.

- **`case 'apartamento':`**
  - **`if consumo_mensal < 10`:** Consumo econômico — excelente controle de água.
  - **`elif consumo_mensal >= 10 e consumo_mensal <= 25`:** Consumo moderado — dentro do padrão residencial.
  - **`else`:** Consumo excessivo — alerta para adoção de medidas de economia e verificação de vazamentos.

- **`case 'casa':`**
  - **`if consumo_mensal <= 25`:** Consumo moderado — dentro do padrão residencial.
  - **`else`:** Consumo excessivo — alerta para adoção de medidas de economia e verificação de vazamentos.

- **`case _:`**
  - **Tratamento de Exceção:** Captura qualquer entrada diferente das opções válidas e exibe uma mensagem de opção inválida.

---

**Desenvolvido por:** Miguel Gonçalves
