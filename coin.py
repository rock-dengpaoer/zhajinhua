import random



def main():
    a = 0

    all = 0
    for i in range(10000000000):
        result = random.randint(0, 1)
        if result == 0:
            a += 1
        all += 1

    print(a / all)

if __name__ == "__main__":
    main()