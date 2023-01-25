from datetime import datetime
import json
from os import path


class CreditCard:
    def __init__(self, card_name, bank_name, card_category, credit_limit, due_date, annual_fee, date_approved):
        self.card_name = card_name
        self.bank_name = bank_name
        self.card_category = card_category
        self.credit_limit = credit_limit
        self.annual_fee = annual_fee
        self.due_date = due_date
        self.date_approved = date_approved
        self.credit_cards = {}

    def add_credit_card(self, card_name, bank_name, card_category, credit_limit, due_date, annual_fee, date_approved):
        self.credit_cards[card_name] = {
            "card_name": card_name,
            "bank_name": bank_name,
            "card_category": card_category,
            "credit_limit": credit_limit,
            "annual_fee": annual_fee,
            "due_date": due_date,
            "date_approved": date_approved,
        }
        print(self.credit_cards)
        self.add_json()

    def add_json(self):

        filename = '/Users/davlatsirojitdinov/Desktop/GIT/CreditCards/credit_cards_dictionary_copy.json'

        # Check if file exists
        if path.isfile(filename) is False:
            raise Exception("File not found")

        # Read JSON file
        with open(filename, "r") as file:
            data = json.load(file)

        # Modify data
        data.append(self.credit_cards)

        # Overwrite file
        with open(filename, "w") as outfile:
            json.dump(data, outfile, indent=4, default=str, separators=(',', ': '))
        print('Successfully appended to the JSON file')

        # Creating a new json file
        # j = json.dumps(self.credit_cards, indent=4, default=str)
        # with open('credit_cards_dictionary.json', 'w') as f:
        #     f.write(j)
        #     f.close()




card_name = input("Enter the name of the credit card: ")
bank_name = input("Enter the name of the Bank: ")
card_category = input("Enter Personal, Business or Authorised User : ")
credit_limit = int(input("Enter the credit limit of the card: "))
due_date = int(input("Enter the due date dd: "))
annual_fee = int(input("Enter the annual fee of the card: "))
date_approved = input("Enter the mm/yyyy of approval: ")


card = CreditCard(card_name, bank_name, card_category, credit_limit, due_date, annual_fee, date_approved)
card.add_credit_card(card_name, bank_name, card_category, credit_limit, due_date, annual_fee, date_approved)
