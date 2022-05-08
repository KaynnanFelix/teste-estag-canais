class Account:
    def __init__(self, name, agencia, conta, cpf):
        self.name = name
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf

    def validate_accounts_for_transfer(self, receiver_account):
        if(self.conta == receiver_account.conta and self.agencia == receiver_account.agencia):
            return True
        return False
