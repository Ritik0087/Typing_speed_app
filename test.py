def gross_wpm(chr, tim, e):
    wpm = (chr / 5) / tim
    net_wpm = (wpm - e) / tim
    return wpm


time = 30 / 60

para1 = 'my name is ritik rastogi and right now i m going some '"important"' work on my laptop.'
para2 = 'my name is ritik rastogi and right now i m going some '"important"' work on my laptop.'

s1 = para1.lower()
s2 = para2.lower()

list1 = s1.split()
list2 = s2.split()
print(list1)

errors = 0

for i in range(len(list1)):
    if list1[i] == list2[i]:
        continue
    else:
        errors += 1

result = gross_wpm(len(para2), time, errors)

print(f'Total Type Characters : {len(para2)}')
print(f'Errors : {errors}')
print(f'Time : {time} min')
print('=' * 30)
print(f'WPM : {result}')
print('=' * 30)

#
# if para1 == para2:
#     print('[*] Passed')
# else:
#     print('[!] Failed')
#     p1 = para1.split()
#     p2 = para2.split()
