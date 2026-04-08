''' #RECURSIVE FUNCTIONS
---------------------
Recursion is a programming technique where a function calls itself, either directly or indirectly,
to solve a problem by breaking it into smaller and simpler subproblems.

It is especially useful for problems that can be divided into identical smaller tasks,
such as mathematical calculations, tree traversals, and divide-and-conquer algorithms. 


def correct_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit PIN: ")
        
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("✔️ Welcome to the ATM")
            return True
        else:
            self.remaining_attempts -= 1
            
            if self.remaining_attempts > 0:
                print(f"❌ Invalid PIN. Attempts left: {self.remaining_attempts}")
            else:
                print("⚠️ Card blocked. Please contact customer")
                return False


sentence = "Python is a  Programming Language"
empty = []
empty_1 = []

def vowel_con(sentence):
    for i in sentence:
        if i.isalpha():   # avoid spaces
            if i in "AEIOUaeiou":
                empty.append(i)
            else:
                empty_1.append(i)
    
    print(f"{empty} these are all vowels in the string")
    print(f"{empty_1} these are all consonants in the string")

vowel_con(sentence) '''


# prime numbers
num = int(input("Enter a Number : "))
count = 0

def prime_num(num):
    count = 0
    
    if num <= 1:
        print(f"{num} is not a prime")
    else:
        for j in range(1, num + 1):
            if num % j == 0:
                count += 1
        
        if count == 2:
            print(f"{num} is a prime")
        else:
            print(f"{num} is not a prime")

prime_num(num)


#evercode in functions task 0 1 and pin changetask 2

