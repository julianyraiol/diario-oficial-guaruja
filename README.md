# Diário Oficial da Cidade de Guarujá/SP

Faz o download dos diários oficiais da cidade de Guarujá-SP

Fonte: [Diário Oficila de Guarujá](http://www.guaruja.sp.gov.br/edicoes-diario-oficial/)

### Instalação

Este projeto requer **Python 3.+** e outras bibliotecas. Utilize uma [virtualenv](https://felipetoscano.com.br/ambientes-virtuais-em-python-com-pyenv-virtualenv-no-ubuntu/) para manter seu ambiente de desenvolvimento.

 Após isso, faça uso do arquivo **requirements.txt** para instalar as dependências

```bash
$ git clone https://github.com/julianyraiol/diario-oficial-guaruja.git
$ cd diario-oficial-guaruja
$ pip install -r requirements.txt
```

Também é necessário ter o Selenium em seu computador. Veja como baixar o driver do selenium para seu navegador [aqui](https://selenium-python.readthedocs.io/installation.html)

Mova o executável para */usr/bin*.

### Executar

No seu terminal, já tendo executado o arquivo de instalação, execute o seguinte comando:

```bash
$ python crawler.py
```


