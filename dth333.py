import random


class Cipher:
    def __init__(self):
        self.__key = random.randint(1, 100)

    def __encrypt(self, num):
        return num * self.__key

    def encrypt_numbers(self, numbers):
        return [self.__encrypt(num) for num in numbers]

    def decrypt_number(self, encrypted_num):
        return encrypted_num / self.__key

cipher = Cipher()
numbers = [10, 20, 30, 40, 50]

encrypted_numbers = cipher.encrypt_numbers(numbers)
print("Зашифровані числа:", encrypted_numbers)

decrypted_number = cipher.decrypt_number(encrypted_numbers[0])
print("Розшифроване число:", decrypted_number)