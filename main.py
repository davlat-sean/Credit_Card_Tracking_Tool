class CreditCard:
    def __init__(self, card_name, credit_limit, annual_fee, due_date):
        self.card_name = card_name
        self.credit_limit = credit_limit
        self.annual_fee = annual_fee
        self.due_date = due_date
        self.balance = 0
        self.credit_cards = {}

    def add_credit_card(self, card_name, credit_limit, annual_fee, due_date):
        self.credit_cards[card_name] = {
            "card_name": card_name,
            "credit_limit": credit_limit,
            "annual_fee": annual_fee,
            "due_date": due_date,
            "balance": 0
        }
        print(self.credit_cards)

card_name = input("Enter the name of the credit card: ")
credit_limit = input("Enter the credit limit of the card: ")
annual_fee = input("Enter the annual fee of the card: ")
due_date = input("Enter the due date of the card: ")

card = CreditCard(card_name, credit_limit, annual_fee, due_date)
card.add_credit_card(card_name, credit_limit, annual_fee, due_date)