# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Hun Sen", 80, "Phnom Penh", "Kmher")  # name, age, city, country
    hobbies = []

    # Your code here
    print("1 Display into, 2 Add hobby, 3 Remove hobby, 4 Edit age, 5 Exit")
    choice = input("What do you want to do?: ")

    if choice == "1":
       print("Name: ", person[0])
       print("Age: ", person[1])
       print("City: ", person[2])
       print("Country: ", person[3])
       print("Hobbies: ", hobbies)

    elif choice == "2":
        hobby = input("Insert new hobby: ")
        hobbies.append(hobby)

    elif choice == "3":
        del hobbies[0]

    age = int(input("Insert new age: "))
    person_list = list(person) # ["Hun sen", 72, "Phnom Penh", "Kmher"]
    person_list[1] = age
    person = tuple(person_list)
    s

if __name__ == "__main__":
    personal_info_manager()