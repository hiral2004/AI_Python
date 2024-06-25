def fibonacci(n):
  sequence=[0, 1]
  while len(sequence) < n:
    next_value= sequence[-1] + sequence[-2]
    sequence.append(next_value)
  return sequence

num_terms=20
fib_sequence=fibonacci(num_terms)
print('Fibonacci sequence with {num_terms} terms is: {fib_sequence}'  .format(num_terms=num_terms, fib_sequence=fib_sequence))
