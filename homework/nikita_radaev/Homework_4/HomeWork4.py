my_dict = {}
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = [6, 7, 8, 9, 10]
my_dict['dict'] = {'one': 12, 'two': 13, 'three': 14, 'four': 15, 'five': 16}
my_dict['set'] = {17, 18, 19, 20, 21}
print(my_dict['tuple'][-1])
my_dict['list'].append('boo')
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'test'
my_dict['dict'].pop('one')
my_dict['set'].add(22)
my_dict['set'].pop()
print(my_dict)
