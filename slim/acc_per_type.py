test_path = '../../../data/test.txt'
test_path_pred = 'test_results.txt'

with open(test_path, 'r') as f:
    test = f.read().split()

with open(test_path_pred, 'r') as f:
    test_pred = f.read().split()

results = {}
assert(len(test) == len(test_pred))
for i in range(0, len(test), 2):
    class_name = test[i].split('/')[0]
    if class_name in results.keys():
        if test[i+1] == test_pred[i+1]:
            results[class_name] = results[class_name] + 1
    else:
        if test[i+1] == test_pred[i+1]:
            results[class_name] = 1
        else:
            results[class_name] = 0

with open('test_acc_per_type.txt', 'a') as f:
    for class_name, count in results.items():
        f.write('{0}: {1:.2f}%'.format(class_name, round(count / 50.0 * 100), 2) + '\n')
