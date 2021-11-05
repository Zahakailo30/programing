class Validation:

    def validate_lett(lett):
        if not str(lett).isalpha():
            raise ValueError("error")
        return lett

    def validate_num(num):
        if not str(num).isnumeric():
            raise ValueError("error")
        return num

    def val_passangers(x = None):
        if x == None:
            x = input()
        if x < 1 or x > 300:
            print("Incorrect! Try again:")

        return x
