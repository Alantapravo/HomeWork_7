N = int(input('Введіть ширину трикутника: '))
print('#1')
for i in range(N):
    print('*' * (N - i))
print('#2')
for i in range(N):
    print('*' * (i + 1))
print('#3')
for i in range(N):
    print(f"{' ' * i}{'*' * (N - i)}")
print('#4')
for i in range(N):
    print(f"{' ' * (N - (i + 1))}{'*' * (i+1)}")




