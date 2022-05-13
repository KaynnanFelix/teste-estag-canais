from messages import error_message, success_message


def validation_pix(valor_transferencia):
    if (valor_transferencia <= 0.00):
        print(error_message('valor de transferência menor ou igual R$ 0,00'))
        return False
    elif(valor_transferencia > 5000.00):
        print(error_message('valor de transferência maior que R$ 5.000,00'))
        return False
    else:
        print(success_message(-valor_transferencia, valor_transferencia))
        return True


def validation_ted(valor_transferencia):
    if(valor_transferencia < 5000.00):
        print(error_message('valor menor que R$ 5.000,00'))
        return False
    elif(valor_transferencia > 10000.00):
        print(error_message('valor maior que R$ 10.000,00'))
        return False
    else:
        print(success_message(-valor_transferencia, valor_transferencia))
        return True


def validation_doc(valor_transferencia):
    if (valor_transferencia >= 10000.00):
        print(success_message(-valor_transferencia, valor_transferencia))
        return True
    else:
        print(error_message('valor de transferência é menor que R$ 10.000,00'))
        return False


class Transaction:
    def __init__(self, id_transferencia, valor_transferencia, tipo_transferencia):
        self.id_transferencia = id_transferencia
        if(self.validation(valor_transferencia, tipo_transferencia)):
            self.valor_transferencia = valor_transferencia
            self.tipo_transferencia = tipo_transferencia

    def validation(self, valor_transferencia, tipo_transferencia):
        if (tipo_transferencia == 'PIX'):
            validation_pix(valor_transferencia)
        elif (tipo_transferencia == 'TED'):
            validation_ted(valor_transferencia)
        elif (tipo_transferencia == 'DOC'):
            validation_doc(valor_transferencia)
        else:
            print(error_message('opção de tranferênca não valida'))
            return False
