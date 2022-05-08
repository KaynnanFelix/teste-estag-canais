def success_message(saldo_emissor, saldo_receptor):
    message = 'Sua transferência foi realizada com sucesso!\nSaldo do emissor: R$ {:.2f}\nSaldo do receptor: R$ {:.2f}\n'.format(
        saldo_emissor, saldo_receptor)
    return message


def error_message(error):
    message = 'Sua transferência não foi completada pois {}.\n'.format(error)
    return message
