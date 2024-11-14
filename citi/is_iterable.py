from collections.abc import Iterable

def is_iterable(obj: object)->bool:
    return isinstance(obj, Iterable)

print(is_iterable([1,2,3]))
print(is_iterable(1))
print(is_iterable("abcd"))

print("===================================")
def check_iterable(obj: object)->bool:
    try:
        iter(obj)
        return True
    except TypeError as te:
        print('Exception occurred : ', str(te))
        return False

print(check_iterable([1,2,3]))
print(check_iterable(1))
print(check_iterable("abcd"))