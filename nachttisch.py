def main():
    import string
    from random import shuffle
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    shuffle(key)
    is_running = True
    print(chars)
    print(key)

    while is_running:
        def get_position():
            if choice == "1":
                wort = input("Gib ein Wort ein welches encrypted werden soll: ")
                for buchstabe in wort:
                    position.append(chars.index(buchstabe))
                return wort
            else:
                wort = input("Gib ein Wort ein welches decrypted werden soll: ")
                for buchstabe in wort:
                    position.append(key.index(buchstabe))
                return wort

        def crypt(position, key, chars, encrypted, decrypted):
            if choice == "1":
                for zahl in position:
                    encrypted.append(key[zahl])
                encrypted = "".join(encrypted)
                print(f'Das ist dein wort: "{wort}" encrypted: "{encrypted}"')
                return encrypted

            else:
                for zahl in position:
                    decrypted.append(chars[zahl])
                decrypted = "".join(decrypted)
                print(f'Das ist dein wort: "{wort}" decrypted: "{decrypted}"')
                return decrypted

        def shufflee(key):
            shuffle(key)
            print("Key wurde erneuert")
            return key

        def beenden():
            if choice == "4":
                is_running = False
                return is_running

        choice = input("Möchtest du encrypten (1), decrypten (2), den Key erneuern (3) oder verlassen (4)?: ")

        position = []
        encrypted = []
        decrypted = []

        if choice == "1" or choice == "2":
            wort = get_position()
            crypt(position, key, chars, encrypted, decrypted)
        elif choice == "3":
            key = shufflee(key)
        elif choice == "4":
            is_running = beenden()
        else:
            print(f' "{choice}" Ist keine valide Angabe!')

if __name__ == "__main__":
    main()