import hashlib

def crack(hash_to_crack):
    for i in range(100000):
        pin = f"{i:05d}"
        current_hash = hashlib.md5(pin.encode()).hexdigest()

        if current_hash == hash_to_crack:
            return pin

    return None

if __name__ == '__main__':
    real_pin_1 = input("Введіть PIN: ")
    hash_1 = hashlib.md5(real_pin_1.encode()).hexdigest()

    result_1 = crack(hash_1)
    print(f"Знайдений PIN: {result_1}")
