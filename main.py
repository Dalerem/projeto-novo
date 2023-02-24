import time
import aspose.pdf as pdf
from PyPDF2 import PdfReader
import requests
import pandas as pd
from playwright.sync_api import sync_playwright

class Interface:

    # Função Construtor
    def __init__(self):
        self.df = "cliente.pdf"
        self.link = "https://esaj.tjsp.jus.br/esaj/portal.do?servico=740000"
        self.url = "https://esaj.tjsp.jus.br/sajcas/login?service=https%3A%2F%2Fesaj.tjsp.jus.br%2Fesaj%2Fj_spring_cas_security_check"
        self.df2 = pd.read_excel("login.xlsx")

    # Função ler PDF
    def ler_pdf(self):
        ler = PdfReader(self.df)
        pagina = ler.pages[0]
        texto = pagina.extract_text()

        print(texto)

    # Função converte
    def converte(self):

        # Carrega o documento PDF
        tabela = pdf.Document(self.df)

        # Inicializa o ExcelSaveOptions
        excelSaveOptions = pdf.ExcelSaveOptions()

        # Converte o PDF para Excel
        tabela.save("cliente.xlsx", excelSaveOptions)

        print("Processo de conversao completo!")

    # Função ler site
    def ler_site(self):
        site = requests.get(self.link)

        print(site.content)

    # Função logar
    def login(self):

        for index, row in self.df2.iterrows():
            print("index: " + str(index) + " E o nome do fulano é " + str(row["SENHA"]))

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                pagina = browser.new_page()
                pagina.goto(self.url)

                time.sleep(2)
                # Preenche o campo CPF
                pagina.fill("#usernameForm", str(row["CPF"]))
                # Preenche o campo SENHA
                pagina.fill("#passwordForm", str(row["SENHA"]))

                # Clica no botão enviar
                #pagina.click("")

                time.sleep(3)
                browser.close()

    # Função de escolha
    def loop(self):
        while True:
            cmd = input('\n1 - Ler o pdf\n2 - Converter para excel\n3 - Ler site\n4 - login\n0 - Sair\n')
            if cmd == '1':
                self.ler_pdf()
            elif cmd == '2':
                self.converte()
            elif cmd == '3':
                self.ler_site()
            elif cmd == '4':
                self.login()
            elif cmd == '0':
                print("Programa finalizado!")
                break
            else:
                print('Não entendi!')
                continue

if __name__ == '__main__':
    interface = Interface()
    interface.loop()