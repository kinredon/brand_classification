with open('../../../data/test.txt', 'r') as f:
    test = f.read().split()

with open('../../../data/test_list.txt', 'a') as f:
    for i in range(0, len(test), 2):
        f.write(test[i] + '\n')
