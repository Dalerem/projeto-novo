import aspose.pdf as pdf

class Interface:

    # Simulação de processos do site de requisição
    processos = [10222021, 20322022, 30452023, 40372019, 50402020, 60332018, 70112021, 80672016]

    # Função converte
    def converte(self):

        # Carrega o documento PDF
        tabela = pdf.Document("cliente.pdf")

        # Inicializa o ExcelSaveOptions
        excelSaveOptions = pdf.ExcelSaveOptions()

        # Converte o PDF para Excel
        tabela.save("cliente.xlsx", excelSaveOptions)

        print("Processo de conversao completo!")

    # Função logar
    def login_pessoas(self):  # Login
        nome = input('Qual seu nome?\n')
        senha = input('Qual sua senha?\n')

        print('login realizado!')

    # Função listar
    def lista_processo(self):
        for i, processo in enumerate(self.processos):
            print(i, processo)

    # Função de escolha
    def loop(self):
        while True:
            cmd = input('\n1 - Login\n2 - Converter\n3 - Listar processos\n0 - Sair\n')
            if cmd == '1':
                self.login_pessoas()
            elif cmd == '2':
                self.converte()
            elif cmd == '3':
                self.lista_processo()
            elif cmd == '0':
                print("Programa finalizado!")
                break
            else:
                print('Não entendi!')
                continue

if __name__ == '__main__':
    interface = Interface()
    interface.loop()