#x = int(input("Input 1st number from sequence\n"))
#y = int(input("2d:\n"))
#z = int(input("3d:\n"))
#mod = int(input("input Mod:\n"))

# 268 411 253 
# 268a + c = 411 mod 499
# 411a + c = 253 mod 499
#
#

x = 268
y = 411
z = 253
mod = 499

current_a = 0
current_c = 0

for c in range(1, mod):
    for a in range(1, mod):
        eq1 = x*a + c # = y
        eq2 = y*a + c # = z
        if( ((eq1 % mod) == y) and ((eq2 % mod) == z) ):
            current_a = a
            current_c = c

            print("a =", current_a)
            print("c =", current_c)
            break
        
x2 = z
print ("X2 = {}".format(x2))

x3 = (current_a * x2 + current_c) % mod
print ("X3 = {}".format(x3))

x4 = (current_a * x3 + current_c) % mod
print ("X4 = {}".format(x4))