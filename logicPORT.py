# Function to simulate OR Gate
def OR(A, B):
	return A | B

print("OR: ")
print("Output of 0 OR 0 is", OR(0, 0))
print("Output of 0 OR 1 is", OR(0, 1))
print("Output of 1 OR 0 is", OR(1, 0))
print("Output of 1 OR 1 is", OR(1, 1))

# Function to simulate AND Gate
def AND(A, B):
	return A & B

print("AND: ")
print("Output of 0 AND 0 is", AND(0, 0))
print("Output of 0 AND 1 is", AND(0, 1))
print("Output of 1 AND 0 is", AND(1, 0))
print("Output of 1 AND 1 is", AND(1, 1))

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2
print("NOT: ")
print("Output of NOT 0 is", NOT(0))
print("Output of NOT 1 is", NOT(1))

# Function to simulate AND Gate
def AND(A, B):
	return A & B;

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2

# Function to simulate NAND Gate
def NAND(A, B):
	return NOT(AND(A, B))

print("NAND: ")
print("Output of 0 NAND 0 is", NAND(0, 0))
print("Output of 0 NAND 1 is", NAND(0, 1))
print("Output of 1 NAND 0 is", NAND(1, 0))
print("Output of 1 NAND 1 is", NAND(1, 1))

# Function to calculate OR Gate
def OR(A, B):
	return A | B;

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2

# Function to simulate NOR Gate
def NOR(A, B):
	return NOT(OR(A, B))

print("NOR: ")
print("Output of 0 NOR 0 is", NOR(0, 0))
print("Output of 0 NOR 1 is", NOR(0, 1))
print("Output of 1 NOR 0 is", NOR(1, 0))
print("Output of 1 NOR 1 is", NOR(1, 1))

# Function to simulate XOR Gate
def XOR(A, B):
	return A ^ B

print("XOR: ")
print("Output of 0 XOR 0 is", XOR(0, 0))
print("Output of 0 XOR 1 is", XOR(0, 1))
print("Output of 1 XOR 0 is", XOR(1, 0))
print("Output of 1 XOR 1 is", XOR(1, 1))