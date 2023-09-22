## Projeto: Tradutor de Texto com PySide6

## Autor: Michael Douglas P Lima
## Contato: michaelsjmvr@hotmail.com
## LinkedIn: [michael-douglas-640a11180](https://www.linkedin.com/in/michael-douglas-640a11180/)


### Visão Geral
- Este é um projeto simples de um tradutor de texto que utiliza a biblioteca PySide6 para criar uma interface gráfica e a biblioteca googletrans para realizar as traduções. O objetivo deste aplicativo é permitir ao usuário inserir um texto em inglês e obter sua tradução para o português. Abaixo, está uma explicação detalhada do projeto:

### Componentes da Interface
- A interface do aplicativo é composta por três elementos principais:

  1. **Campo de Texto Original**: Um campo de entrada de texto onde o usuário pode inserir o texto em inglês que deseja traduzir.

  2. **Campo de Tradução**: Uma área de texto de leitura apenas onde a tradução para o português será exibida após a tradução.

  3. **Botão "Traduzir"**: Um botão que inicia o processo de tradução quando clicado.

### Funcionamento
- Ao abrir o aplicativo, o usuário encontra um campo de entrada de texto rotulado como "Texto Original". Nesse campo, o usuário pode inserir o texto em inglês que deseja traduzir.

- Após inserir o texto, o usuário pode clicar no botão "Traduzir". O aplicativo utiliza a biblioteca googletrans para enviar o texto ao Google Translate, que realiza a tradução do inglês para o português. O resultado da tradução é exibido no campo de "Tradução".

- Se ocorrer algum erro durante o processo de tradução, uma mensagem de erro será exibida no campo de "Tradução" para informar o usuário sobre o problema.

### Como Executar o Aplicativo
- Para executar o aplicativo, siga as instruções abaixo:

  1. Certifique-se de ter Python instalado em seu sistema.

  2. Instale as bibliotecas necessárias executando o seguinte comando:

    ```
    pip install PySide6 googletrans==4.0.0-rc1
    ```

  3. Copie e cole o código do projeto em um arquivo Python (.py).

  4. Execute o arquivo Python usando o Python 3:

     ```
     python tradutor_de_textos.py
     ```

  5. O aplicativo será iniciado e você poderá usar a interface para inserir e traduzir textos em inglês.

- Este projeto é um exemplo simples de como criar uma interface gráfica para uma aplicação de desktop em Python e como realizar traduções de texto usando a biblioteca googletrans. Você pode personalizá-lo ou expandi-lo para atender às suas necessidades específicas.
