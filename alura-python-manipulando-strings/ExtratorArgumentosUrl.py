class ExtratorArgumentoUrl:


    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = str(url).lower()
        else:
            raise AttributeError("Url inválida!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def urlEhValida(url):
        PREFIXO_URL = 'https://bytebank.com/'
        return bool(url) and url.startswith(PREFIXO_URL)

    def extrairArgumentos(self, argumento):
        separador = "="
        conector_de_argumentos = "&"
        index_inicio = self.url.find(argumento+separador) + len(argumento) + len(separador)
        index_fim = self.url.find(conector_de_argumentos, index_inicio)
        return self.url[index_inicio:index_fim]