from faker import Faker
import random
import pandas as pd

fake = Faker('en_IN')


def generator(n):
    transactions = []
    for i in range(n):
        transaction_id = fake.uuid4()
        account_number = fake.bban()
       
        date = fake.date_this_year()
        time = fake.time()
        cust_id = fake.uuid4()
        merchant = fake.company()
       
        location_rec = fake.city()
        location_send = fake.city()
        card_type = fake.random_element(['Visa','MasterCard','Discover'])
        transaction_type = fake.random_element(["purchase", "withdrawal", "transfer", "payment"])
        card_number = fake.credit_card_number(card_type=card_type.lower())
        device_id = fake.uuid4()
        ip_address = fake.ipv4()
        channel = fake.random_element(['online','in-store','mobile'])
        international = fake.boolean(chance_of_getting_true=10)
        previous_transaction_amount = round(random.uniform(10.0, 10000.0), 2)
        balance_before = round(random.uniform(1000.0, 50000.0), 2)
        transaction_amount = round(random.uniform(1000.0,balance_before),2)
        balance_after = balance_before - transaction_amount
        is_fraud = random.choices([0, 1], weights=[50, 50])[0]

        transactions.append({
            "TransactionID": transaction_id,
            "Date":date,
            "Time":time,
            "AccountNumber": account_number,
            "CustomerID": cust_id,
            "TransactionAmount": transaction_amount,
            "Merchant": merchant,
            "LocationRec": location_rec,
            "LocationSend":location_send,
            "TransactionType": transaction_type,
            "CardType": card_type,
            "CardNumber": card_number,
            "DeviceID": device_id,
            "IPAddressSender": ip_address,
            "Channel": channel,
            "IsInternational": international,
            "PreviousTransactionAmount": previous_transaction_amount,
            "BalanceBefore": balance_before,
            "BalanceAfter": balance_after,
            "IsFraud": is_fraud
        })
    return transactions

n = 100000
transactions = generator(n)
df = pd.DataFrame(transactions)

df.to_csv("fraud_synthetic.csv")
print("done")
