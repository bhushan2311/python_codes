
from file1_imp import a
print("a",a)
from file1_imp import add
print("Addition",add(12,12))
from file1_imp import mul
print("Multiplication",mul(7,7))
# from file1_imp import b             # will show erroe as b is inside __name__=__main__
# print(b)

# ------- preferable method--------
import file1_imp            #imported our custom module file1

print(file1_imp.a)
print(file1_imp.add(2,3))      # imported add fun from custom module file1
print(file1_imp.mul(4,3))      # imported lambda mul function from custom module file1
# print(file1_imp.b)           # will show erroe as b is inside __name__=__main__

# import snake_water_gun     # imported snake_water_gun as module
#
# snake_water_gun.Comp
# snake_water_gun.human
# snake_water_gun.Tied
# z=snake_water_gun.Human
# snake_water_gun.gun(z)