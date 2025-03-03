# Defining the sets based on the Venn diagram
A = {'a', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'i', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'j', 'k'}

# a. How many elements are in both A and B?
A_and_B = A & B  # Intersection of A and B
print(f"Elements in both A and B: {A_and_B}, Count: {len(A_and_B)}")

# b. How many elements are in B that are NOT in A or C?
B_only = B - (A | C)  # Elements in B but not in A or C
print(f"Elements in B but not in A and C: {B_only}, Count: {len(B_only)}")

# c. Using set operations to express given sets:
print("i.  {h, i, j, k}: ", (B & C) | {'i', 'j', 'k'})  
print("ii.  {c, d, f}: ", C)  
print("iii.  {b, c, h}: ", B & A | {'h'})  
print("iv. {d, f}: ", C - {'c'})  
print("v.  {c}: ", A & B & C)  
print("vi.  {l, m, o}: ", B - (A | C))  
