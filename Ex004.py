a = input("Digite algo: ")
print(f"O tipo primitivo disso é {type(a)}")
print(f"É somente espaços? {a.isspace()}")
print(f"É um número? {a.isnumeric()}")
print(f"É alfabético? {a.isalpha()}")
print(f"É alfanumérico? {a.isalnum()}")
print(f"Está em maiúsculas? {a.isupper()}")
print(f"Está em minúsculas? {a.islower()}")
print(f"A primeira letra é maiúscula? {a.istitle()}")
