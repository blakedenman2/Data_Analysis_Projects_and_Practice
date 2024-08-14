def main():
    sentence = input("What is the answer to the great question of life, the universe, and everything? ")
    if clean(sentence) == "42" or clean(sentence) == "Forty-Two":
        print("Yes")
    else: print("No")



def clean(answer):
    answer = "-".join(answer.split())
    answer = answer.title()
    return answer

main()
