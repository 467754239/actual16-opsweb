import random


def generate_verification_code():
    """
    :return: Random generated code
    """
    return str(int(random.random() * 10000)).zfill(4)
