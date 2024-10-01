def count_vowels(s):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)
