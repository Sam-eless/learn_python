class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []

    def __repr__(self):
        return f"Player ({self.user_name}, {self.used_words})"

    def count_used_words(self):
        """Получение количества использованных слов (возвращает int)"""
        return len(self.used_words)

    def add_to_used(self, word):
        """Добавление слова в использованные слова (ничего не возвращает)"""
        self.used_words.append(word)

    def is_usage_before(self, word):
        """Проверка использования данного слова до этого (возвращает bool)"""
        if word in self.used_words:
            return True
        else:
            return False
