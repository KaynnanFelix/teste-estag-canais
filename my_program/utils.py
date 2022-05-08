from messages import error_message


def is_header(line):
    try:
        if(line == 'id_transferencia|valor_transferencia|tipo_transferencia|nome_emissor|agencia_emissor|conta_emissor|cpf_emissor|nome_receptor|agencia_receptor|conta_receptor|cpf_receptor\n'):
            return True
        else:
            return False
    except:
        print('An exception occurred in the is_header function.')


def is_empty_line(line):
    try:
        if(line == '\n'):
            return True
        else:
            return False
    except:
        print('An exception occurred in the is_empty_lin function.')


def is_data_valid(data):
    if (len(data) == 11):
        return True
    else:
        return False


def convert_data_entry_to_dictionary_format(data):
    tmp = {
        'tipo_transferencia': data[2],
        'nome_emissor': data[3],
        'agencia_emissor': data[4],
        'conta_emissor': data[5],
        'cpf_emissor': data[6],
        'nome_receptor': data[7],
        'agencia_receptor': data[8],
        'conta_receptor': data[9],
        'cpf_receptor': data[10]
    }

    data[10] = data[10].replace('\n', '')
    if not data[0]:
        tmp['id_transferencia'] = None
    else:
        tmp['id_transferencia'] = int(data[0])
    if not data[1]:
        tmp['valor_transferencia'] = None
    else:
        tmp['valor_transferencia'] = float(data[1])

    return tmp
