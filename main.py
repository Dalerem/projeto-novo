import time
import aspose.pdf as pdf
from PyPDF2 import PdfReader
import pandas as pd
from playwright.sync_api import sync_playwright

class Interface:
    # Função Construtor
    def __init__(self):
        # Documento cliente em pdf
        self.df = "cliente.pdf"
        # Url da pagina login
        self.url = "https://esaj.tjsp.jus.br/sajcas/login?service=https%3A%2F%2Fesaj.tjsp.jus.br%2Fesaj%2Fj_spring_cas_security_check"
        # Dataframe do documento login em xlsx
        self.df2 = pd.read_excel("login.xlsx")
        # Url da pagina consulta de processo do 1º grau
        self.url2 = "https://esaj.tjsp.jus.br/cpopg/open.do"
        # Dataframe do documento processo em xlsx
        self.df3 = pd.read_excel("processo.xlsx")

    # Função ler PDF
    def ler_pdf(self):
        # Abrir o PDF
        ler = PdfReader(self.df)
        # Acessar a primeira pagina do PDF
        pagina = ler.pages[0]
        # Ler o conteudo
        texto = pagina.extract_text()

        print(texto)
        print("Sucesso!")

    # Função converte o PDF para Excel
    def converte(self):
        # Carrega o documento PDF
        tabela = pdf.Document(self.df)

        # Inicializa o ExcelSaveOptions
        excelSaveOptions = pdf.ExcelSaveOptions()

        # Converte o PDF para Excel
        tabela.save("cliente.xlsx", excelSaveOptions)

        print("Processo de conversao completo!")

    # Função faz o login no site
    def login(self):
        for index, row in self.df2.iterrows():
            print("index: " + str(index) + " E o nome do fulano é " + str(row["SENHA"]))

            with sync_playwright() as p:
                # Abre o navegador
                browser = p.chromium.launch(headless=False)
                # Cria uma pagina nova
                pagina = browser.new_page()
                # Acessa a url
                pagina.goto(self.url)

                time.sleep(2)
                # Preenche o campo CPF
                pagina.fill("#usernameForm", str(row["CPF"]))
                # Preenche o campo SENHA
                pagina.fill("#passwordForm", str(row["SENHA"]))

                # Clica no botão buscar
                #pagina.click("#pbEntrar")

                time.sleep(3)
                browser.close()

    # Função numero do processo
    def processos(self):
        for index, row in self.df3.iterrows():
            print("index: " + str(index) + " E o numero do processo é: " + str(row["PROCESSO"]) +
                  "Com terminacao: " + str(row["TERMINACAO"]))

            with sync_playwright() as p:
                # Abre o navegador
                browser2 = p.chromium.launch(headless=False)
                # Cria uma pagina nova
                pagina2 = browser2.new_page()
                # Acessa a url2
                pagina2.goto(self.url2)

                # Espera 2 seguntos para preencher o campo
                time.sleep(2)
                # Preenche o campo numero do processo
                pagina2.fill("#numeroDigitoAnoUnificado", str(row["PROCESSO"]))
                # Peenche o campo numero unificado
                pagina2.fill("#foroNumeroUnificado", str(row["TERMINACAO"]))

                # Clica no botão consultar
                #pagina2.click("#botaoConsultarProcessos")

                # Espera 3 segundos para fechar o browser
                time.sleep(3)
                # Fecha a browser
                browser2.close()

    # Função de escolha
    def loop(self):
        while True:
            cmd = input('\n1 - Ler o pdf\n2 - Converter para excel\n3 - login\n4 - Numero do processo\n0 - Sair\n')
            if cmd == '1':
                self.ler_pdf()
            elif cmd == '2':
                self.converte()
            elif cmd == '3':
                self.login()
            elif cmd == '4':
                self.processos()
            elif cmd == '0':
                print("Programa finalizado!")
                break
            else:
                print('Não entendi!')
                continue

if __name__ == '__main__':
    interface = Interface()
    interface.loop()
