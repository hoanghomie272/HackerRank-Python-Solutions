def minion_game(string):
    vowels = "AEIOU"
    word_S, word_K = 0, 0
    n = len(string)
    
    for i in range(n):
        if string[i] in vowels:
            word_K += (n - i)
        else:
            word_S += (n - i)
    
    if word_S > word_K:
        print(f"Stuart {word_S}")
    elif word_K > word_S:
        print(f"Kevin {word_K}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)

