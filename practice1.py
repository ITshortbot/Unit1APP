class Py:
    @staticmethod
    def duplicate(a, x) -> bool:
        if a in x:
            return True
        else:
            return False
    
obj = Py()
print(obj.duplicate(2, {1, 0, 3}))
