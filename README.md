# Professor Virtual de Inglês

Esta é uma aplicação web simples desenvolvida com Flask que utiliza a API da OpenAI para criar um professor virtual de inglês. O usuário pode enviar perguntas em inglês e receber respostas automáticas, simulando uma conversa com um professor.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para a criação do backend.
- **Flask**: Framework web utilizado para criar o servidor e as rotas.
- **OpenAI API**: Usada para gerar respostas automáticas com o modelo GPT-3.5.
- **HTML/CSS**: Para o frontend e a interface do usuário.

## Pré-requisitos

1. **Python 3.7+** deve estar instalado.
2. **Conta na OpenAI** e uma chave de API para acessar o modelo GPT-3.5.

## Como Configurar o Projeto

1. **Clone este repositório**:

    ```bash
    git clone https://github.com/seu-usuario/professor-virtual-ingles.git
    cd professor-virtual-ingles
    ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configuração da chave da API**:

    - Crie um arquivo `.env` no diretório raiz do projeto.
    - Adicione sua chave da OpenAI ao arquivo `.env` no seguinte formato:

    ```plaintext
    OPENAI_API_KEY=sua_chave_aqui
    ```

5. **Estrutura do Projeto**

    Certifique-se de que a estrutura do projeto segue este formato:

    ```
    project_folder/
    ├── app.py                # Arquivo principal Flask
    ├── key.env               # Contém a chave da API
    ├── requirements.txt      # Dependências do projeto
    ├── static/
    │   └── styles.css        # Arquivo CSS para estilizar a página
    └── templates/
        └── index.html        # Página HTML do projeto
    ```

## Como Executar o Projeto

1. **Inicie o servidor Flask**:

    ```bash
    python app.py
    ```

2. **Acesse o aplicativo** no seu navegador em:

    ```
    http://localhost:5500
    ```

## Estrutura do Código

### Arquivo `app.py`

- **Carrega a chave da API** usando o pacote `dotenv` para segurança.
- **Define uma função `chat_gpt`** para enviar uma mensagem ao modelo da OpenAI e receber uma resposta.
- **Rota `/`**:
  - Exibe a página inicial (`index.html`) onde o usuário pode enviar uma pergunta.
  - Processa a resposta do modelo e exibe na interface.

### Arquivo `index.html`

- Página principal com um campo de entrada para o usuário digitar perguntas e um botão de envio.
- Exibe a resposta do professor virtual em um `textarea` somente leitura.

### Arquivo `styles.css`

- Contém o estilo para o layout da página.
- Centraliza a página, estiliza o formulário e ajusta o `textarea` para exibir as respostas.

## Exemplo de Uso

Após iniciar o servidor e abrir o navegador, você verá a interface onde pode digitar perguntas em inglês. O professor virtual responderá com orientações ou respostas automáticas.
