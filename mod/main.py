
from collection import Collection

def main():
    info = Collection("text.txt")
    info.read_from_file()
    print(
        "'1'- to see all information "
          "'2'- to add a new request"
          "'3'- to end program"
    )
    option = int(input())
    if option == 1:
        print(info)
    elif option == 2:
        info.add_req()
    elif option == 3:
        exit()

main()

