import cryptography.fernet as fernet

"""Fernet is a symmetric encryption algorithm, a part of the cryptography library in Python. It is based on the 
Advanced Encryption Standard (AES) in cipher block chaining (CBC) mode and a Message Authentication Code (MAC) based 
on HMAC-SHA256. Fernet allows you to encrypt and decrypt data using a shared secret key, making it a useful tool for 
secure transmission of sensitive information. """


def encrypt_file(input_file, output_file, key):
    """
    Crypt a file specified in input using a keyword, output is also specified
    :param input_file:
    :param output_file:
    :param key:
    :return:

    input_file = "example.txt"
    encrypted_file = "example_encrypted.txt"
    key = "my secret key"

    # encrypt the file
    encrypt_file(input_file, encrypted_file, key)
    """
    with open(input_file, "rb") as f:
        file_data = f.read()

    fernet_key = fernet.Fernet(key.encode())
    encrypted_data = fernet_key.encrypt(file_data)

    with open(output_file, "wb") as f:
        f.write(encrypted_data)


def decrypt_file(input_file, output_file, key):
    """
    De-crypt an input file into another specified in input using a specific keyword
    :param input_file:
    :param output_file:
    :param key:
    :return:

    encrypted_file = "example_encrypted.txt"
    decrypted_file = "example_decrypted.txt"
    key = "my secret key"

    # decrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)
    """
    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    fernet_key = fernet.Fernet(key.encode())
    decrypted_data = fernet_key.decrypt(encrypted_data)

    with open(output_file, "wb") as f:
        f.write(decrypted_data)


