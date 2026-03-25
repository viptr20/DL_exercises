
age = 16

def is_adult (age):
    if age >= 18:
        return True
    else:
        return False
    
def is_adult2 (age):
    return True if age >= 18 else False

print(is_adult(age))
print(is_adult2(age))


