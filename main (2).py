E={0, 2, 4, 6, 8}
N={1, 2, 3, 4, 5}

union_EN=E.union(N)
intersection_EN=E.intersection(N)
difference_EN=E.difference(N)
symmetric_difference_EN=E.symmetric_difference(N)

print(f'Union of E and N is {union_EN}')
print(f'Intersection of E and N is {intersection_EN}')
print(f'Difference of E and N is {difference_EN}')
print(f'Symmetric Difference of E and N is {symmetric_difference_EN}') 