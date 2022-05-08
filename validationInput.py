from messages import error_message


def isValid(data):

    if not data['id_transferencia']:
        print(error_message('id_transferencia não foi informado'))
        return False

    if not data['valor_transferencia']:
        print(error_message('valor_transferencia não foi informado'))
        return False

    if not data['tipo_transferencia']:
        print(error_message('tipo_transferencia não foi informado'))
        return False

    if not data['nome_emissor']:
        print(error_message('nome_emissor não foi informado'))
        return False

    if not data['agencia_emissor']:
        print(error_message('agencia_emissor não foi informado'))
        return False

    if not data['conta_emissor']:
        print(error_message('conta_emissor não foi informado'))
        return False

    if not data['cpf_emissor']:
        print(error_message('cpf_emissor não foi informado'))
        return False

    if not data['nome_receptor']:
        print(error_message('nome_receptor não foi informado'))
        return False

    if not data['agencia_receptor']:
        print(error_message('agencia_receptor não foi informado'))
        return False

    if not data['conta_receptor']:
        print(error_message('conta_receptor não foi informado'))
        return False

    if not data['cpf_receptor']:
        print(error_message('cpf_receptor não foi informado'))
        return False

    return True
