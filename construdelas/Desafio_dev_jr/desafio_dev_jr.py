import pandas as pd
from os import path
import win32com.client as win32

print("""   Acompanhamento do jogo!
      **************************
      MENU DE OPÇÕES:
      [1] para inserir
      [2] para consultar
      [3] para exportar em arquivo Excel
      [4] para encerrar""")
resumo = []
cont = 0
opcao = 0
maxi = 0
mini = 1000
qmini = 0
qmaxi = 0

while opcao != 4:
    with open('resumo_dos_jogos.xlsx', 'a+') as arquivo:
        arquivo = df
    opcao = int((input('Digite a opção desejada de acordo com o Menu:')))
    if opcao == 1:
        cont += 1
        pontuacao = int(input('Digite os pontos do último jogo'))
        if cont == 1:
            lista = [1, pontuacao, pontuacao, pontuacao, 0, 0]
            mini = pontuacao
            maxi = pontuacao
            resumo.append(lista)
        else:
            if pontuacao > maxi:
                maxi = pontuacao
                qmaxi += 1
            if pontuacao < mini:
                mini = pontuacao
                qmini += 1
            lista = [cont, pontuacao, mini, maxi, qmini, qmaxi]
            resumo.append(lista)

        pastaUsuario = path.join(path.expanduser('~'))
        # print('#Gera a planilha a partir dos dados obtidos usando um dataframe e depois convertendo em excel')
        df = pd.DataFrame(resumo)
        df.rename(columns={0: 'Jogo',
                           1: 'Placar',
                           2: 'Mínimo da temporada',
                           3: 'Máximo da temporada',
                           4: 'Quebra de recorde min.',
                           5: 'Quebra de recorde máx'
                           }, inplace=True)
        df.to_excel(pastaUsuario + '\\resumo_dos_jogos.xlsx', index=False)
        # print('Planilha salva com sucesso no diretório - ' + pastaUsuario + '\\resumo_dos_jogos.xlsx')


    elif opcao == 2:
        dados = pd.read_excel(pastaUsuario + '\\resumo_dos_jogos.xlsx')
        print(dados)

    elif opcao == 3:
        # criar a integração com o outlook
        outlook = win32.Dispatch('outlook.application')
        # criar um email
        email = outlook.CreateItem(0)
        jogador = input('Digite o nome do jogador: ')
        assinatura = input('Digite o nome do responsável pelo envio desse email: ')
        anexo = pastaUsuario + '\\resumo_dos_jogos.xlsx'
        # "C:/Users/amand/resumo_dos_jogos.xlsx"
        # configurar as informações do seu e-mail
        email.To = "amandaomariano@hotmail.com"
        email.Subject = "E-mail automático do Python"
        email.Attachments.Add(anexo)
        email.HTMLBody = f"""
<p>Olá, segue o resumo de desempenho dos jogos de {jogador}.</p>
<p>Abs,</p>
<p>Atenciosamente, {assinatura}</p>
"""
        email.Send()
        print("Email Enviado")

    else:
        print('Opção inválida. Tente novamente')
        print('Fim do programa. Obrigado(a). Até a próxima')

        """Fazer uma lista de dicionários em que cada indice da lista é um dicionario com as respectivas chaves"""