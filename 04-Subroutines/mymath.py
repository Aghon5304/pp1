import random
def generate_number():
    return random.randrange(1,10)
if __name__ == "__main__":
    for x in range(30):
        print(generate_number())