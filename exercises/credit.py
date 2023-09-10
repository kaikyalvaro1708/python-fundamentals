def main():
    accounts = [
        ("AMEX", "378282246310005"),
        ("AMEX", "371449635398431"),
        ("MASTERCARD", "5555555555554444"),
        ("MASTERCARD", "5105105105105100"),
        ("VISA", "4111111111111111"),
        ("VISA", "4012888888881881"),
        ("INVALID", "1234567890")
    ]

    userNumber = input("Number: ")

    #Percorrer toda a tupla e verifica se o segundo elemento elemento é igual ao input
    found_accounts = [account[0] for account in accounts if account[1] == userNumber]

    if found_accounts:
        print("Account: ".join(found_accounts))
    else:
        print("Try again")

if __name__ == "__main__":
    main()
