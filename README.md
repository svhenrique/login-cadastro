## Configuração do ambiente 

### Clonando repositório

Para clonar o repositório é possível baixa-lo completamente do github e extrair em uma pasta de projeto ou utilizar o comando:

```bash
https://github.com/svhenrique/login-cadastro.git
```

Para utilizar o comando anterior é necessário ter o Git instalado no computador.

### Configurando ambiente 

É necessária a instalação da linguagem Python. É possível baixa-la aqui:

- https://www.python.org/downloads/

Passo a passo da instalação da linguagem pode ser encontrado aqui:

- https://wiki.python.org/moin/BeginnersGuide/Download

É recomendável que se use um ambiente virtual para utilização da aplicação. Mas antes, é preciso baixar a biblioteca virtualenv e para fazer isso, basta executar o comando:


```bash
pip install virtualenv
```

Para criar um ambiente virtual no python, fazemos:

```bash
virtualenv venv
```

Após criar o ambiente virtual, se você estiver no prompt de comando (shell, terminal, cmd, etc), é preciso ativar o venv (ambiente virtual) criado, para isso utilizamos o comando:

```bash
venv/bin/activate
```

## Instalando dependências

Para instalar dependências, basta usar o comando:

```bash
pip install -r requirements.txt
```
## Configurando .env

Crie um arquivo de texto e nomeio para ".env", ou utilize o env.example (lembre-se de renomear para ".env"), e salve na pasta raiz do projeto. Após isso, você verá o seguinte:

```bash
SECRET_KEY=
SENDGRID_API=
EMAIL=
```

Do lado direito das variáveis, será necessário colocar em SECRET_KEY (fornecida ao criar um projeto Django), SENDGRID_API (uma API key do SendGrid, com a permissão de MAIL SEND ativado) e EMAIL (um domínio de email autenticado pelo SendGrid)

### Como adquirir a SECRET_kEY

- Iniciando um novo projeto django com:

```bash
django-admin startproject projeto 
```

Copia o hash guardado na variável SECRET_KEY no arquivo settings.py (fazer processo de coleta de SECRET_KEY em outra pasta e em outro ambiente virtual para assegurar o encapsulamento da aplicação) e cola na SECRET_KEY do .env.

- Usando a função get_random_secret_key():

Com o Django instalado, execute o comando

```bash
python manage.py shell
```

no shell, importe a função get_random_secret_key com o comando

```bash
from django.core.management.utils import get_random_secret_key
```

e utilize a função usando

```bash
get_random_secret_key()
```

copie o valor retornado e cole na SECRET_KEY do .env.

### Como adquirir a SENDGRID_API

1 - É necessário se cadastrar no SendGrid e ter um domínio de email (sender), autenticado ou não, fornecido pela plataforma. Para se cadastrar acesse 

- https://sendgrid.com/

e procure a opção Sign In, preencha os dados e cadastre-se.

2 - Após se cadastrar, é necessário criar um sender, para isso, acesse

https://docs.sendgrid.com/ui/sending-email/senders

e siga os passos comentados.

3 - Depois de seguir os passos 1 e 2, é preciso criar uma API Key do SendGrid, na tela inicial do SendGrid, vá em Settings e abra a página API Keys. Nela, clique em Create API Key e marque Restricted Acess, após isso, procure e ative a opção Mail Send, clique em Create e View para finalizar a criação da API.

Se todos os passos foram feitos corretamente uma API aparecerá na tela, copie e cole ao lado direito de SENDGRID_API. 

Vídeo mostrando o que se deve fazer no passo 3:
- https://www.youtube.com/watch?v=xCCYmOeubRE

### Como adquirir o EMAIL

Se você já fez a parte do SENDGRID_API, basta usar o sender criado, colando ao lado direito de EMAIL. 

Como criaar um sender:
- https://docs.sendgrid.com/ui/sending-email/senders





