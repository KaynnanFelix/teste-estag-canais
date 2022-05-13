from account import Account
from transaction import Transaction
from messages import error_message
from utils import convert_data_entry_to_dictionary_format, is_data_valid, is_empty_line, is_header
from inputValidation import all_data_informed


with open('entrada.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if (is_header(line)):
            continue

        if(is_empty_line(line)):
            continue

        data = line.split('|')
        if(is_data_valid(data)):
            result = convert_data_entry_to_dictionary_format(data)
            if(all_data_informed(result) == False):
                continue

            sender_account = Account(
                result['nome_emissor'], result['agencia_emissor'], result['conta_emissor'], result['cpf_emissor'])
                
            receiver_account = Account(
                result['nome_receptor'], result['agencia_receptor'], result['conta_receptor'], result['cpf_receptor'])

            if(sender_account.validate_accounts_for_transfer(receiver_account)):
                print(error_message(
                    'não é possível efetuar transferência para a mesma conta'))
                continue

            transaction = Transaction(
                result['id_transferencia'], result['valor_transferencia'], result['tipo_transferencia'])

        else:
            print(error_message(
                'não foi informado todos os dados necessários para efetuar transação'))
