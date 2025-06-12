N = int(input())
S = input()

# Create a set of allowed characters from the bitmask
allowed_chars = set()

for i in range(26):  # From bit 0 to bit 25
    if (N >> i) & 1:
        allowed_chars.add(chr(ord('A') + i))

# Check if all characters in S are in the allowed set
if all(c in allowed_chars for c in S):
    print("YES")
else:
    print("NO")
