import textwrap
import os
from datetime import datetime

class Bank:
  balance = 0
  daily_limit = 5
  daily_withdrawal = 0
  limit_value = 500
  extract = ''


  def __init__(self):
    pass


  def deposit(self , value , extract , balance):
    self.value = value
    self.extract = extract
    add_deposit = balance + value
    date = datetime.now()
    date_txt = date.strftime("‘%d/%m/%Y %H:%M’")
    extract = f'\n================================ \n Tipo de Operação: Deposito \n Valor: R${value},00 \n Horário: {date_txt} \n'
    return add_deposit , extract


  def to_withdraw(self , balance ,  value ,  extract):
    self.balance = balance
    self.value = value
    self.extract = extract
    add_withdraw = balance - value

    date = datetime.now()
    date_txt = date.strftime("‘%d/%m/%Y %H:%M’")
    extract = f'\n ================================ \n Tipo de Operação: Saque \n Valor: R${value},00 \n Horário: {date_txt} \n'

    return add_withdraw , extract


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
  while True:
    menu_option = menu()

    if menu_option == 'q':
      os.system('cls')
      break

    elif menu_option == 'd':
      os.system('cls')
      date = datetime.now()
      date_txt = date.strftime("‘%d/%m/%Y %H:%M’")

      value_deposite = int(input('Digite o Valor Que Deseja Depositar:\n => '))
      deposit, extract = Bank().deposit(value=value_deposite , extract= Bank.extract , balance=Bank.balance)

      os.system('cls')
      print(f'Deposito Feito com sucesso!\n Valor: R${value_deposite} \n Horário: {date_txt}')
      Bank.balance = deposit
      Bank.extract = extract

    elif menu_option == 's':
      os.system('cls')

      if Bank.daily_limit > Bank.daily_withdrawal:
        value_withdrawal = int(input('Digite o Valor que Deseja Sacar: \n => '))

        flag = True if value_withdrawal <= Bank.balance else False

        if (flag is True) and (value_withdrawal <= 1000):
          date = datetime.now()
          date_txt = date.strftime("‘%d/%m/%Y %H:%M’")

          withdraw , extract = Bank().to_withdraw(balance= Bank.balance , value=value_withdrawal , extract= Bank.extract )

          os.system('cls')


          print(f'Saque Feito com sucesso!\n Valor: R${value_withdrawal} \n Horário: {date_txt}')

          Bank.daily_withdrawal += 1
          Bank.balance = withdraw
          Bank.extract += extract


        elif flag is False:
          print(f'@@@ Não foi possivel completar a Transação. Saldo Insuficiente! Seu saldo é  R${Bank.balance}  @@@')

        elif value_withdrawal > 1000:
          print(f'@@@ Você excedeu o Limite de Valor por Saque! Valor limite R${Bank.limit_value}  @@@')
      else:
        print(f'@@@ Você excedeu o Limite de Saques Diários @@@')

    elif menu_option == 'e':
      os.system('cls')

      extract_list = f'================ EXTRATO ================ \n @@@ Seu Saldo é R${Bank.balance},00 @@@\n {Bank.extract}'
      print(extract_list)

main()
