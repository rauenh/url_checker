### Este é um projeto que verifica a conectividade de URLs inseridas pelo usuário.

**Como rodar o projeto:**<br/>
* Passo 1: Clonar o repositório<br/>
* Passo 2: Criar o ambiente virtual para o projeto, <br/>
No windows:  ``python -m venv venv``<br/>
No Linux/macOS: ``python -m venv venv``<br/>
* Passo 3: Ativar o ambiente virtual<br/>
No Windows: ``venv\Scripts\activate``<br/>
No Linux/macOS: ``source venv/bin/activate``<br/>
* Passo 4: Instalar as dependências com o pip ``python -m pip install aiohttp``

**Os arquivos:** <br/>
  *  __init__.py permite que a pasta rpchecker seja lida como um Pacote do Python
  * __main__.py funciona como a função inicial que vai executar o programa de verificação de URLs
  * checker.py é onde estão localizadas as funcionalidades chave da aplicação 
  * cli.py é onde estão os comandos da interface com o usuário (Facilitaria a comunicação com um projeto front-end por exemplo)

**Rodando o pacote:**<br/>
* Abra o terminal na pasta que você clonou e digite o seguinte comando
``python -m urlchecker -h``
* Irá aparecer as seguintes informações:
![screenshot do terminal mostrando as opções do programa urlchecker](
