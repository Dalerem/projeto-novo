import aspose.pdf as pdf
from PyPDF2 import PdfReader

class Interface:

    df = "cliente.pdf"

    # Função logar
    def login_pessoas(self):
        nome = input('Qual seu nome?\n')
        senha = input('Qual sua senha?\n')

        print('login realizado!')

    def ler_pdf(self):
        ler = PdfReader(self.df)
        number_of_pages = len(ler.pages)
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

    # Função de escolha
    def loop(self):
        while True:
            cmd = input('\n1 - Login\n2 - Ler o pdf\n3 - Converter para excel\n0 - Sair\n')
            if cmd == '1':
                self.login_pessoas()
            elif cmd == '2':
                self.ler_pdf()
            elif cmd == '3':
                self.converte()
            elif cmd == '0':
                print("Programa finalizado!")
                break
            else:
                print('Não entendi!')
                continue

if __name__ == '__main__':
    interface = Interface()
    interface.loop()