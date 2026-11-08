#Criar classe Anúncio
#Criar classe Plataforma
#Usa dados da tabela? Método. Se não, função.

import csv

class Plataforma:

    #Construtor
    def __init__(self):
        self.anuncios = []
        self.anuncios_lidos = 0
        self.anuncios_validos = 0
        self.anuncios_invalidos = 0
        self.anuncios_ausentes = 0
        self.media_preco = 0
        self.media_area = 0
        self.media_comodos = 0
        self.media_preco_m2 = 0

    def adicionar_anuncio(self, endereco, codigo_postal, preco, area, comodos, lon, lat):
        anuncio = Anuncio(endereco, codigo_postal, preco, area, comodos, lon, lat)
        anuncio.transformar_dados()
        anuncio.m2 = anuncio.criar_m2()
        self.anuncios.append(anuncio)

    def processar_base(self):

        # Iterar sobre cada linha do conteúdo do CSV
        for anuncio in self.anuncios:
            self.anuncios_lidos += 1

            if anuncio.preco and anuncio.codigo_postal and anuncio.comodos and anuncio.lon and anuncio.lat:
                self.anuncios_validos += 1

                if not anuncio.preco or not anuncio.area or not anuncio.comodos or not anuncio.lon or not anuncio.lat:
                    self.anuncios_ausentes += 1
            else:
                self.anuncios_invalidos += 1
    def calcular_medias(self):

        #Calcular totais
        total_preco = 0
        total_area = 0
        total_comodos = 0
        total_m2 = 0

        for anuncio in self.anuncios:
            if anuncio.preco:
                total_preco += anuncio.preco
            if anuncio.area:
                total_area += anuncio.area
            if anuncio.comodos:
                total_comodos += anuncio.comodos
            if anuncio.m2:
                total_m2 += anuncio.m2

        #Calcular médias
        if self.anuncios_validos > 0:
            self.media_preco = total_preco / self.anuncios_validos
            self.media_area = total_area / self.anuncios_validos
            self.media_comodos = total_comodos / self.anuncios_validos
            self.media_preco_m2 = total_m2 / self.anuncios_validos

class Anuncio:
        
    #Construtor
    def __init__(self, endereco, codigo_postal, preco, area, comodos, lon, lat):
        self.endereco = endereco
        self.codigo_postal = codigo_postal
        self.preco = preco
        self.area = area
        self.comodos = comodos
        self.lon = lon
        self.lat = lat
        self.m2 = None
    
    def transformar_dados(self):

        #Transformar tipos de dados para manipulação
        if self.preco:
            if self.preco != "NA":
                self.preco = float(self.preco)
            else:
                self.preco = None
        if self.area:
            if self.area != "NA":
                self.area = float(self.area)
            else:
                self.area = None
        if self.comodos:
            if self.comodos != "NA":
                self.comodos = int(self.comodos)
            else:
                self.comodos = None
        if self.lon:
            if self.lon != "NA":
                self.lon = float(self.lon)
            else:
                self.lon = None
        if self.lat:
            if self.lat != "NA":
                self.lat = float(self.lat)
            else:
                self.lat = None

    def  criar_m2(self):
        if self.area and self.preco:
            self.m2 = self.preco / self.area
        else:
            self.m2 = None

def carregar_dados():

    #Carregar os dados do arquivo csv
    try:
        with open("HousingPrices-Amsterdam-August-2021.csv", "r") as arquivo:
            dados = csv.DictReader(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    else:

        #Criar instâncias
        plataforma1 = Plataforma()
        for linha in dados:
            plataforma1.adicionar_anuncio(
                linha["Address"],
                linha["Zip"],
                linha["Price"],
                linha["Area"],
                linha["Room"],
                linha["Lon"],
                linha["Lat"]
            )
        return plataforma1