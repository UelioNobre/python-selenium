# Python Selenium

#### Baixar imagem docker para uso
```bash
docker pull selenium/standalone-firefox:106.0
```


#### Rodando a imagem
```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size 2g --name firefox selenium/standalone-firefox:106.0
```

Caso ocorra algum problema, tentar baixar a versão da imagem, de 106.0 para 105.0


#### Reiniciando imagem docker
```bash
docker restart firefox
```

### Instalação da biblioteca `selenium`
```bash
pip install selenium
```

### Executando o script pela primeira vez
```bash
python index.py
```
