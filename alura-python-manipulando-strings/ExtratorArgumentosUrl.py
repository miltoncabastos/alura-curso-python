class ExtratorArgumentoUrl:


    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = str(url).lower()
        else:
            raise LookupError("Url inválida!")

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