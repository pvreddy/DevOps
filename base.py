width = 5
for num in range(5,12): 
    for base in 'dXob':
        print base
        print('{0:{width}{base}}'.format(num, base=base, width=width))
    print()
