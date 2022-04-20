# 1. Print odds 1-20
#       Using a loop write code that will console.log all of the odd values from 1 up to 20.

for i in range(21):
    print(i)
print('Challenge 1 Complete')
# 2. Decreasing Multiples of 3
#       Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0.
#       Print the sequence

for i in range(101):
    if i % 3 == 0:
        print(i)
print('Challenge 2 Complete')

# 3. Using a loop write code that will console.log the values in this sequence 4, 2.5, 1, -0.5, -2, -3.5.
seq = ['4', '2.5', '1', '-0.5', '-2', '-3.5']

for i in range(len(seq)):
    print(seq[i])
print('Challenge 3 Complete')

# 4. Write code that will add all of the values from 1-100 onto some 
#      variable sum and at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100. We should get back 5050 at the end.
n=0
for i in range(101):
    n += i
print(n)
print('Challenge 4 Complete')

# 5. Factorial
#   Write code that will multiply all of the values from 1-12 onto some variable product and 
#       at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end.

n=2
for i in range(3,13):
    n *= i
print(n)
print('Challenge 5 Complete')
