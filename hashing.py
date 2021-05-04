def hash2(m, p):
    m_str = str(m)
    h = len(m_str)
    for digit in m_str:
        h = (int(digit) + 2 * h + 1)**2 % (p-1)
    return h+1


class Hasher:
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def __init__(self):
        self.alphabet_dict = {}
        self.create_alphabet_dict()

    # ------------------------------------------------------------------------------------------------------------------
    # Заполняет словарь при инициализации класса
    # ------------------------------------------------------------------------------------------------------------------
    def create_alphabet_dict(self):
        for i in range(len(self.alphabet)):
            self.alphabet_dict[self.alphabet[i]] = i+1

    # ------------------------------------------------------------------------------------------------------------------
    # Хэшировани сообщения по первому алгоритму Васильевой
    # ------------------------------------------------------------------------------------------------------------------
    def hash1(self, msg):
        h = len(msg)
        for letter in msg:
            h = (self.alphabet_dict[letter.upper()] + h)**2 % 79
        return h
