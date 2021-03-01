def long_name(name):
    if len(name) > 14:
        return True
    return False


print("Please enter your name:")
name = input()
is_long = long_name(name)
if is_long:
    print("The name {} is long!".format(name))
else:
    print("The name {} is short!".format(name))
