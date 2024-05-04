import textwrap

def menu():
  menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [ls] Listar contas
    [nu] Novo usuário
    [q] Sair
  => """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

  if valor > 0:
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado !!!!")
  else:
    print("Valor inválido. Depósito não realizado!!!")
        
  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques > limite_saques

  if excedeu_saldo:
    print("Saldo insuficiente!!!")
  elif excedeu_limite:
    print("Valor do saque excede limite.")
  elif excedeu_saques:
    print("Quantidade diária de saque excedida.")
  elif valor > 0:
    saldo -= valor
    extrato += f"Saque:    R$ {valor*-1:.2f}\n"
    numero_saques += 1
    print("Saque realizado !!!")
  else:
    print("Valor é inválido. Saque não realizado!!!")

  return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
  print("======================= EXTRATO =======================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("=======================================================")

def criar_usuario(usuarios):
  cpf = input("Digite o CPF (somente numeros): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("CPF já foi utilizado.")
    return
  
  nome = input("Nome completo: ")
  data_nascimento = input("Data de nascimento: dd--mm-aaaa: ")
  endereco = input("Endereço completo (Logradouro, Nro - Bairro - Cidade/UF): ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

  print("Usuario criado com sucesso !!!")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Digite o CPF: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criado com sucesso !!!")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  
  print("Usuário não encontrado. Operação não realizada !!!")

def listar_contas(contas):
  for conta in contas:
    linha = f"""
      Agência: {conta["agencia"]}
      C/C: {conta["numero_conta"]}
      Titular: {conta["usuario"]["nome"]}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu()

    if opcao == "d":
      valor = float(input("Valor do depósito: "))

      saldo, extrato = depositar(saldo, valor, extrato)


    elif opcao == "s":
      valor = float(input("Valor do saque: "))

      saldo, extrato = sacar(
        saldo = saldo,
        valor = valor,
        extrato = extrato,
        limite = limite,
        numero_saques = numero_saques,
        limite_saques = LIMITE_SAQUES,
      )

    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
        
    elif opcao == "lc":
      listar_contas(contas)

    elif opcao == "q":
      break
    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")

main()