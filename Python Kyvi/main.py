# Passos:
# 1. Importar o App e o Builder (GUI)
# 2. Criar o aplicativo (Python)
# 3. Criar a função build (Kivy)

import requests
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("screen.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI


    def on_start(self):
        self.root.ids["um"].text = f""
        self.root.ids["dois"].text = f""


    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()
