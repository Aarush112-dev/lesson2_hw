list = [5,15,3,14,24,48,54,68,72,94,100]

question = int(input("What number are you searching for in the list? "))

def linear_search(n):
    count = 0
    while count < len(list):
        if list[count] == n:
            print(f"The number {n} has been found at index {count}.")
            return
        elif n != list[count]:
            count += 1
    else:
        print(f"The number {n} was not found in the list.")
            

linear_search(question)
