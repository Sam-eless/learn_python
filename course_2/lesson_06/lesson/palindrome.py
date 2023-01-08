def is_palindrome(word):
    word.lower()
    word.replace(" ", "")

    if word == word[::-1]:
      return True
    else:
      return False




try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")
