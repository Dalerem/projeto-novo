import aspose.pdf as pdf
from PyPDF2 import PdfReader
import requests

class Interface:

    # Função Construtor
    def __init__(self):
        self.df = "cliente.pdf"
        self.link = "https://esaj.tjsp.jus.br/esaj/portal.do?servico=740000"

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
    def login_pessoas(self):
        nome = input('Qual seu nome?\n')
        senha = input('Qual sua senha?\n')

        print('login realizado!')

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
                self.login_pessoas()
            elif cmd == '0':
                print("Programa finalizado!")
                break
            else:
                print('Não entendi!')
                continue

if __name__ == '__main__':
    interface = Interface()
    interface.loop()