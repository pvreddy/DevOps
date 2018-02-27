def staircase(n):
    for stairs in range(1, n + 1):
        print ' ' * (n - stairs) + '#' * stairs

n = int(raw_input("enter value of n: "))

staircase(n)
