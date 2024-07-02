from OurErrors import OurFirstError


def add(num1, num2):
    if num1 is not int or num2 is not int:
        raise TypeError("the parameters must be numbers")
    if num1 < 0 or num2 < 0:
        raise ValueError("the numbers must be bigger than 0")
    return num1 + num2


users = ["aaa", "bbb", 2]


def get_user(user_id):
    if user_id == len(users)-1:
        raise IndexError("the id is not valid")
    return users[user_id]


def stam(num):
    if num != 9:
        raise OurFirstError()


if __name__ == "__main__":
    try:
        print(get_user(5))
    except IndexError as e:
        print(e)
    stam(90)
    # print(add("d", 1))
    # print(add(2, -3))
    # print("----")
