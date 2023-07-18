
class AtoZ:
    def __getitem__(self, item):
        if 0 <= item < 26:
            return chr(item + ord('A'))
        # raise IndexError()
        raise SystemError()


for letter in AtoZ():
    print(letter)
print('over')

