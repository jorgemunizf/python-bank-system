# python-bank-system

## Sistema Bancário Simples em Python

Esse é um sistema bancário simples implementado em Python. Ele permite que você execute várias operações, como depósitos, saques, verificação de saldo, criação de novas contas e listagem de contas existentes.

## Classes
- **Cliente:** A classe base para todos os clientes. Ela possui um endereço e uma lista de contas.
  
- **PessoaFisica:** Uma subclasse de **Cliente** que representa uma pessoa física. Ela possui atributos como nome, data de nascimento, CPF e endereço.

- **Conta:** A classe base para todas as contas bancárias. Ela possui atributos como número da conta, agência, cliente e histórico de transações.
- **ContaCorrente:** Uma subclasse de **Conta** que representa uma conta corrente. Ela possui atributos adicionais como limite de cheque especial e número máximo de saques.
- **Historico:** Uma classe que mantém o histórico de todas as transações realizadas em uma conta.
- **Transacao:** Uma classe base abstrata para todas as transações. Ela possui uma propriedade de valor e um método de registro.
- **Saque e Deposito:** Subclasses de "**Transacao**" que representam transações de saque e depósito, respectivamente.

## Funções

- **menu():** Exibe o menu principal do aplicativo.
- **filtrar_cliente(cpf, clientes):** Filtra os clientes por seu CPF.
- **recuperar_conta_cliente(cliente):** Retorna a primeira conta de um cliente.
- **depositar(clientes):** Permite que um cliente deposite dinheiro.
- **sacar(clientes):** Permite que um cliente saca dinheiro.
- **exibir_extrato(clientes):** Exibe o histórico de transações e o saldo de uma conta de cliente.
- **criar_cliente(clientes):** Cria um novo cliente pessoa física.
- **criar_conta(numero_conta, clientes, contas):** Cria uma nova conta corrente para um cliente.
- **listar_contas(contas):** Lista todas as contas existentes.

## Uso
Para usar o sistema bancário, basta executar o script Python. O menu principal será exibido, permitindo que você execute várias operações.

================ MENU ================<br>
    [d] Depositar<br>
    [s] Sacar<br>
    [e] Extrato<br>
    [nc] Nova conta<br>
    [lc] Listar contas<br>
    [nu] Novo usuário<br>
    [q] Sair<br>
    =>

- Para criar um novo cliente, selecione a opção "nu - Novo usuário" e forneça as informações necessárias.

- Para criar uma nova conta, selecione a opção "nc - Nova conta" e forneça o CPF do cliente.

- Para depositar ou sacar dinheiro, selecione as opções "d - Depositar" ou "s - Sacar", respectivamente, e forneça o CPF do cliente e o valor da transação.

- Para verificar o histórico de transações e o saldo de uma conta, selecione a opção "e - Extrato" e forneça o CPF do cliente.

- Para listar todas as contas existentes, selecione a opção "lc - Listar contas".

- Para sair do aplicativo, selecione a opção "s - Sair".