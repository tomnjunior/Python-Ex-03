import random # importei a biblioteca random
listadoadores = [] # iniciei uma lista vazia para inserir os doadores cadastrados
def cd(nome: str, valordoacao: float):
    listadoadores.extend(((nome + ' ') * int(valordoacao // 10)).split())
    return
# criei uma função que chamei de forma abreviada de "cd" - cadastro de doador.
# com essa função essa lista poderá ser extendida para os doadores que poderão doar novamente no futuro.
# o cálculo valordoacao retorna o valor do cociente inteiro arredondado para baixo do resultado da divisão por 10.
# o nome do doador será atribuido a lista "x" vezes de acordo com o resultado da divisão do valordoacao.

def sorteiolista():
    random.shuffle(listadoadores)
    print(f'Lista Embaralhada: {listadoadores}')
    return random.choice(listadoadores)
# criei uma função que recebe a lista inserida na função "cd" - cadastro de doador e embaralha a lista
# mostra a lista embaralhada e retorna um nome sorteado desta lista.

op = int(input('Deseja cadastrar um novo doador? 0 - Não   1 - Sim '))
# recebe a opção para cadastro de sim ou não.
while op == 1:
    nomedoador = input('Nome: ')
    valortotal = float(input('Valor: '))
    #se a opção 1 foi inserida, o nome e o valor da doação devem ser inseridos.
    while len(nomedoador.strip()) == 0 or valortotal < 10:
        # enquanto o valor for abaixo de 10 ou o nome dado como vazio, o programa.
        # irá pedir para inserir o nome e o valor.
        print('Digite o nome e o valor para doação.')
        nomedoador = input('Nome: ')
        valortotal = float(input('Valor: '))
    cd(nomedoador, valortotal)
    #quando sai do cadastro de nome e valor a função "cd" - cadastro de doador é acionada.
    op = int(input('Deseja cadastrar um novo doador? 0 - Não   1 - Sim'))
    # após o cadastro o programa pergunta novamente se quer cadastrar um novo nome e valor.
    # se o usuário inserir 1 o programa pede novamente o nome e o valor.
    # se o usuário inserir 0 o programa vai para a linha abaixo e mostrará a lista dos doadores
    # a lista embaralhada e o sorteado.
if len(listadoadores) > 0:# a função len devolve o tamanho da lista
    print(f'Lista para sorteio: {listadoadores}')# mostra a lista da doadores embaralhada
    print(f'O nome sorteado foi: {sorteiolista()}')# mostra o nome sorteado