class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"BasicWord ({self.word}, {self.subwords})"

    def check_word(self, user_answer):
        """Проверка введенного слова в списке допустимых подслов (вернет bool)"""
        if user_answer in self.subwords:
            return True
        else:
            return False

    def count_subwords(self):
        """Подсчет количества подслов (вернет int)."""
        return len(self.subwords)
