"""
*** Cadastro Simples ***

Conhecimentos:

Nível de código: 1
Laços: Condicional Simples
Banco de Dados: Nenhum
"""


usuario_bd = usuario = input('Nome de usuário: ')
senha_bd = senha = input('Senha de usuário: ')

print('**Log In**')
usuario_log = input('Usuário: ')
senha_log = input('Senha: ')

if (usuario_bd == usuario_log) and (senha_bd == senha_log):
    print('Você foi logado com sucesso!')
else:
    print('Usuário ou senha inválidos!')