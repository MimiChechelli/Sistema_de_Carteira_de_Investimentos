#painel inicial de acesso:
print('Bem vindo ao Chelli Investimentos!')
while True: 
    x = int(input(('Acesso (1) Investidor ou (2) Mentor: ')))
    if(x==1):
        #todos os invetidores tem acesso a um grupo básico de investimentos 
        #investidores tp II possuem maior rendimento e opções de rendas fixas 
        #tp III em renda variavel e tp I em tesouro direto 
        print("Realize o login:")
        input('Nome:') #deve ser parte da lista de investidores
        input('CPF: ') #deve ser parte da lista de investidores
        print("O que deseja fazer?")
        print('(1) Realizar investimento')
        print('(2) Verificar histórico')
        a = int(input(''))
        if(a==1):
            b = int(input('Deseja investir em tesouro direto (1), renda fixa(2) ou renda variavel(3)? '))
            if(b==1):
                print("a")
            elif(b==2):
                print("a")
            elif(b==3):
                print("a")
        elif(a==2):
            print('Histórico')

    elif(x==2):
        print("Realize o login:")
        input('Nome: ')
        input('Senha: ')
        print('O que deseja fazer?')
        print('(1) cadastrar novos usuarios')
        print('(2) pesquisar usuario')
        c = int(input(("(3) imprimir tudo")))


    z = input('Se deseja finalizar o programa digite "s"... ')
    
'''- cadastro de usuários: funcionário, investidor  (lista de objetos) adc dic com funcionarios e investidores 
que podem ser deletados pelo chefe e pelos funcionarios respectivamente
- simulações de investimentos: aporte de  R$xxx (calcula-se os juros, rendimentos, taxas... baseado no tempo de investimento)  
- previsibilidade dos lucro do investimento (baseado em data de entrada e saída)
- simulação de investimento com renda variável : aporte de R$ xxxxx (variação diária de juros/taxas)
- relatório final com as estatísticas dos investimentos por usuário
- Menu: 1) cadastro, 2) pesquisa (do usuário), 3) alterar, 4)excluir usuário, 5) investimento (5.1. renda fixa, 5.2. renda variável), 6) relatórios'''
