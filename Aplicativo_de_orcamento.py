def duas_casas(num):
    if num // 1 == num / 1:
        return f'{num}.00'
    return f'{num}'

class Category:

    def __init__(self, product):
        self.product = product
        self.ledger = []
        self.money = 0
        self.quantidade_retirada = 0

    def check_funds(self, value):
        if self.money >= value:
            return True
        else:
            return False

    def deposit(self, deposit, description=''):
        self.money += deposit
        self.ledger.append({'amount': deposit, 'description': description})

    def withdraw(self, withdrawn, description=''):
        if self.check_funds(withdrawn):
            self.quantidade_retirada += withdrawn
            self.money -= withdrawn
            self.ledger.append({'amount': -withdrawn, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return self.money

    def transfer(self, transferred, local):
        if self.check_funds(transferred):
            self.money -= transferred
            self.quantidade_retirada += transferred
            self.ledger.append({'amount': -transferred, 'description': f'Transfer to {local.product}'})
            local.money += transferred
            local.ledger.append({'amount': transferred, 'description': f'Transfer from {self.product}'})
            return True
        else:
            return False

    def __str__(self):
        initial = ''
        initial_loop = 0
        quanty = 30 - len(self.product)
        total = 0
        while initial_loop < quanty:
            initial += '*'
            initial_loop += 1
            if quanty // 2 == quanty / 2:
                if initial_loop == (quanty / 2):
                    initial += self.product
            else:
                if initial_loop == (quanty / 2 + 0.5):
                    initial += self.product
        for dic in self.ledger:
          if len(dic['description']) > 23:
            initial += f'\n{"".join(list(dic["description"][:23]))} {duas_casas(dic["amount"])}'
          else:
            initial += f'\n{dic["description"]}' \
                       f'{" "*(30 - len(duas_casas(dic["amount"])) - len(dic["description"]))}' \
                       f'{duas_casas(dic["amount"])}'
          total += dic['amount']
        initial += f'\nTotal: {total}'
        return initial


def create_spend_chart(categorys):
    barras = {100: '', 90: '', 80: '', 70: '', 60: '', 50: '', 40: '', 30: '', 20: '', 10: '', 0: ''}
    media = []
    quantia_total = 0
    nomes_lista = []
    linhas = []
    maior = ''

    for category in categorys:
        quantia_total += category.quantidade_retirada
        nomes_lista.append(list(category.product))
        if len(category.product) > len(maior):
            maior = category.product

    multiplicador = 100 / quantia_total

    for category in categorys:
        media.append(int(category.quantidade_retirada * multiplicador / 10) * 10)

    contagem = 0
    while contagem < len(maior):
        string = ''
        for palavra in nomes_lista:
            try:
                string += f'{palavra[contagem]}  '
            except:
                string += '   '
        linhas.append(string)
        contagem += 1

    nomes = '\n     '.join(linhas)
    contagem_media = 0

    for category in media:
        if category >= 100:
            barras[100] = barras[100].ljust(contagem_media * 3, ' ')
            barras[100] += 'o  '
        if category >= 90:
            barras[90] = barras[90].ljust(contagem_media * 3, ' ')
            barras[90] += 'o  '
        if category >= 80:
            barras[80] = barras[80].ljust(contagem_media * 3, ' ')
            barras[80] += 'o  '
        if category >= 70:
            barras[70] = barras[70].ljust(contagem_media * 3, ' ')
            barras[70] += 'o  '
        if category >= 60:
            barras[60] = barras[60].ljust(contagem_media * 3, ' ')
            barras[60] += 'o  '
        if category >= 50:
            barras[50] = barras[50].ljust(contagem_media * 3, ' ')
            barras[50] += 'o  '
        if category >= 40:
            barras[40] = barras[40].ljust(contagem_media * 3, ' ')
            barras[40] += 'o  '
        if category >= 30:
            barras[30] = barras[30].ljust(contagem_media * 3, ' ')
            barras[30] += 'o  '
        if category >= 20:
            barras[20] = barras[20].ljust(contagem_media * 3, ' ')
            barras[20] += 'o  '
        if category >= 10:
            barras[10] = barras[10].ljust(contagem_media * 3, ' ')
            barras[10] += 'o  '
        barras[0] = barras[0].ljust(contagem_media * 3, ' ')
        barras[0] += 'o  '
        contagem_media += 1

    return f'Percentage spent by category\n100| {barras[100].ljust(contagem_media * 3, " ")}\n ' \
           f'90| {barras[90].ljust(contagem_media * 3, " ")}\n 80| {barras[80].ljust(contagem_media * 3, " ")}' \
           f'\n 70| {barras[70].ljust(contagem_media * 3, " ")}\n 60| {barras[60].ljust(contagem_media * 3, " ")}' \
           f'\n 50| {barras[50].ljust(contagem_media * 3, " ")}\n 40| {barras[40].ljust(contagem_media * 3, " ")}' \
           f'\n 30| {barras[30].ljust(contagem_media * 3, " ")}\n 20| {barras[20].ljust(contagem_media * 3, " ")}\n' \
           f' 10| {barras[10].ljust(contagem_media * 3, " ")}\n  0| {barras[0].ljust(contagem_media * 3, " ")}' \
           f'\n    {"-" * (len(barras[0]) + 1)}\n     {nomes}'
