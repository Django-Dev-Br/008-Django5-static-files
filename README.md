
# 008 Django 5 - Static Files (html, css, java script e imagens)

### O que são Arquivos Estáticos no Django?

Arquivos estáticos no Django referem-se a arquivos que não mudam em resposta às interações do usuário, como CSS, JavaScript e imagens. Eles são essenciais para o design e a funcionalidade de um site, mas não contêm conteúdo dinâmico. No Django, esses arquivos são gerenciados usando a configuração de arquivos estáticos, que permite coletar, servir e referenciar esses arquivos de forma organizada e eficiente. A configuração abaixo é adiciona ao arquivo settings.py do projeto Django.

- **STATIC_URL**: É a URL que refere-se aos arquivos estáticos. No nosso projeto, está definida como `'/static/'`, o que significa que todos os arquivos estáticos estarão acessíveis sob essa URL.

- **STATICFILES_DIRS**: É uma lista de diretórios onde o Django procurará arquivos estáticos adicionais, além da pasta `static/` dentro de cada app. No nosso projeto, foi configurada para incluir a pasta `static/` no diretório raiz do projeto.

- **STATIC_ROOT**: Durante o desenvolvimento, o Django serve arquivos estáticos diretamente. No entanto, em produção, todos os arquivos estáticos devem ser coletados em um único diretório definido por `STATIC_ROOT` e servidos por um servidor web dedicado.

Documentação: [https://docs.djangoproject.com/en/4.0/howto/static-files/](https://docs.djangoproject.com/en/4.0/howto/static-files/)

### Coletando Arquivos Estáticos para Produção

Quando estiver pronto para implantar seu projeto Django em produção, é necessário coletar todos os arquivos estáticos em um único diretório definido por `STATIC_ROOT`. Isso permite que o servidor web sirva esses arquivos de forma eficiente. Para coletar todos os arquivos estáticos, use o comando:

```bash
python manage.py collectstatic
```
Este comando irá procurar todos os arquivos estáticos nos diretórios especificados em `STATICFILES_DIRS` e nas pastas `static/` de cada aplicativo, e copiá-los para o diretório definido por `STATIC_ROOT`.

## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12 com PIP e venv**
- **o Django 5 requer Python 3.10 ou superior.**

- **No [repositório 001](https://github.com/Django-Dev-Br/001-django4-basic-project) há explicações sobre PIP e venv**

  Se necessário, confira o vídeo abaixo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual):
 [![Watch the video](https://img.youtube.com/vi/eetDeQrv0Rs/0.jpg)](https://youtu.be/eetDeQrv0Rs)

### Passos para Executar

1. **Clone o repositório**:
   
    ```bash
    git clone https://github.com/Django-Dev-Br/008-Django5-static-files.git
    ```

3. **Crie  um ambiente virtual no diretório root**:

   **Windows**
    ```bash
     python -m venv myvenv 
    ```
      **Linux**
     ```bash
     python3 -m venv myvenv  
    ```

4. **Ative o ambiente virtual criado**:

   **Windows**
    ```bash
    myvenv\Scripts\activate  
    ```

     **Linux**
    ```bash
    source myvenv/bin/activate  
    ```
    
6. **Acesse a pasta do projeto Django**:
   
    ```bash
    cd 008-Django5-static-files
    ```
    
6. **Instale o Django**:

   Fazer a instalação após a ativação da virtual env fará com que a instalação seja feita nessa pasta ao invés do computador. Isso significa que o pacote Django não estará disponivel para todos os usuários do computador, mas apenas para o contexto no qual essa venv esteja ativada. Veremos sua ativação logo abaixo.

    **Instalação manualmente via gerenciador de dependências PIP**
    ```bash
    pip install django
    ```
    - use, preferencialmente, a versão 5.1. Para tanto, execute o comando:

     ```bash
    pip install  "django>=5.1,<=5.2"
    ```

    ----- **OU** -----

    **Instalação via arquivo requirements**
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo requirements.txt é um arquivo de texto que contém uma lista de pacotes a ser instalado em uma venv. É uma boa prática de programação do ecossistema Python.

    
8. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

9. **Acesse a aplicação no seu navegador**:

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

### Estrutura de Diretórios do Projeto

```
008-django4-static-files/
├── manage.py
├── myapp/
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py           # Contém a função 'index' para renderizar 'index.html'
│   └── templates/
│       └── index.html     # Página HTML que carrega a imagem estática
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Configurações de STATIC_DIRS, STATICFILES_DIRS, STATIC_ROOT
│   ├── urls.py            # URL principal direcionando para 'myapp.views.index'
│   └── wsgi.py
└── static/
    └── myapp/
        └── images/
            └── pythondjango.jpg  # Imagem a ser exibida
├── staticfiles/        # Diretório para onde os arquivos estáticos são coletados quando executamos o comando `collectstatic`
│   ├── admin/          # Arquivos estáticos padrão do Django Admin
│   │   ├── css/        # Arquivos CSS usados pelo painel administrativo
│   │   │   └── vendor/
│   │   │       └── select2/
│   │   ├── img/        # Imagens usadas no painel administrativo
│   │   │   └── gis/
│   │   └── js/         # Arquivos JavaScript usados pelo painel administrativo
│   │       ├── admin/
│   │       └── vendor/
│   │           ├── jquery/
│   │           ├── select2/
│   │           │   └── i18n/
│   │           └── xregexp/
│   └── myapp/          # Arquivos estáticos específicos do app `myapp`
│       └── images/     # Imagens usadas no app `myapp`
```

### Código deste projeto

arquivo: myprojecto/settings.py
```python

STATIC_URL = '/static/'  # Define o caminho base para acessar arquivos estáticos no navegador

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Indica ao Django onde buscar arquivos estáticos adicionais durante o desenvolvimento
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Local onde os arquivos estáticos serão coletados quando executarmos o comando `collectstatic`

```

### Sobre Nosso Treinamento Prático-Profissional com projeto real para iniciantes e avançados em web DevOps Full-stack com Python, Django, Bootstrap e Linux.

[Django Developers Brasil - Aprenda programando enquanto programa aprendendo!](https://django.dev.br/)

Nosso treinamento oferece uma experiência prática de aprendizado de programação, adequada tanto para iniciantes quanto para desenvolvedores avançados. Você participará de um projeto real de desenvolvimento de software em um ambiente corporativo autêntico, onde pessoas com diferentes níveis de conhecimento irão colaborar, aprendendo umas com as outras.

**Junte-se a nós!** E desenvolva as habilidades necessárias para o mercado de trabalho, aprimorando tanto seus conhecimentos técnicos quanto suas soft skills em um ambiente colaborativo e realista.
