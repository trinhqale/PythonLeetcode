def ValidPalindrome(s: str):
    raw_str = "".join(char.lower() for char in s if char.isalnum())
    i, j = 0, len(raw_str) - 1
    while i < j:
        if raw_str[i] != raw_str[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(ValidPalindrome(s1))
    print(ValidPalindrome(s2))
if __name__ == "__main__":
    main()