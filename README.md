
# 008 Django 4 Static Files Example

### O que são Arquivos Estáticos no Django?

Arquivos estáticos no Django referem-se a arquivos que não mudam em resposta às interações do usuário, como CSS, JavaScript e imagens. Eles são essenciais para o design e a funcionalidade de um site, mas não contêm conteúdo dinâmico. No Django, esses arquivos são gerenciados usando a configuração de arquivos estáticos, que permite coletar, servir e referenciar esses arquivos de forma organizada e eficiente. A configuração abaixo é adiciona ao arquivo settings.py do projeto Django.

- **STATIC_URL**: É a URL que refere-se aos arquivos estáticos. No nosso projeto, está definida como `'/static/'`, o que significa que todos os arquivos estáticos estarão acessíveis sob essa URL.

- **STATICFILES_DIRS**: É uma lista de diretórios onde o Django procurará arquivos estáticos adicionais, além da pasta `static/` dentro de cada app. No nosso projeto, foi configurada para incluir a pasta `static/` no diretório raiz do projeto.

- **STATIC_ROOT**: Durante o desenvolvimento, o Django serve arquivos estáticos diretamente. No entanto, em produção, todos os arquivos estáticos devem ser coletados em um único diretório definido por `STATIC_ROOT` e servidos por um servidor web dedicado.

### Coletando Arquivos Estáticos para Produção

Quando estiver pronto para implantar seu projeto Django em produção, é necessário coletar todos os arquivos estáticos em um único diretório definido por `STATIC_ROOT`. Isso permite que o servidor web sirva esses arquivos de forma eficiente. Para coletar todos os arquivos estáticos, use o comando:

```bash
python manage.py collectstatic
```

Este comando irá procurar todos os arquivos estáticos nos diretórios especificados em `STATICFILES_DIRS` e nas pastas `static/` de cada aplicativo, e copiá-los para o diretório definido por `STATIC_ROOT`.

## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12**  
  [Baixar Python 3.12](https://www.python.org/downloads/release/python-3122/)

  Confira o vídeo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual): [Trabalhando com Múltiplas Versões do Python + venv](https://youtu.be/eetDeQrv0Rs?si=rAIDmLCgdeh7ouXa)

- **Virtualenv**

  Para instalar o pacote `virtualenv` no Python, utilize os seguintes comandos:

  - **Linux**:
    ```bash
    python3 -m pip install virtualenv
    ```

  - **Windows**:
    ```bash
    python -m pip install virtualenv
    ```

### Passos para Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Django-Dev-Br/008-Django-4-Static-Files.git
    cd 008-django4-static-files
    ```

2. **Crie um ambiente virtual**:
   
    - **Linux**:
    ```bash
    python3 -m venv myvenv
    ```

  - **Windows**:
    ```bash
    python -m venv myvenv
    ```

3. **Ative o ambiente virtual criado**:
    ```bash
    source myvenv/bin/activate  # Linux
    myvenv\Scripts\activate  # Windows
    ```

4. **Instale o Django**:
    ```bash
    pip install django==4.2.15
    ```

5. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação no seu navegador**:

   Vá para [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e você verá a imagem `pythondjango.jpg` sendo exibida na página inicial.

### Código HTML 

Aqui está o código HTML usado para carregar a imagem estática usando o template `index.html`:

```
{% load static %}  <!-- Carrega a tag 'static' para uso nos caminhos dos arquivos estáticos -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Página Inicial</title>
</head>
<body>
    <h1>Imagem do Python Django</h1>
    <!-- Usa a tag 'static' para definir o caminho da imagem estática -->
    <img src="{% static 'myapp/images/pythondjango.jpg' %}" alt="Python Django">
</body>
</html>

```

### Sobre Nosso Treinamento Prático-Profissional com projeto real para iniciantes e avançados em web DevOps Full-stack com Python, Django, Bootstrap e Linux.

[Django Developers Brasil - Aprenda programando enquanto programa aprendendo!](https://django.dev.br/)

Nosso treinamento oferece uma experiência prática de aprendizado de programação, adequada tanto para iniciantes quanto para desenvolvedores avançados. Você participará de um projeto real de desenvolvimento de software em um ambiente corporativo autêntico, onde pessoas com diferentes níveis de conhecimento irão colaborar, aprendendo umas com as outras.

**Junte-se a nós!** E desenvolva as habilidades necessárias para o mercado de trabalho, aprimorando tanto seus conhecimentos técnicos quanto suas soft skills em um ambiente colaborativo e realista.
