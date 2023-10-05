from functions import write, read


while True:
    user_action = input("\nEnter add, show, edit, complete, exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        user_action = user_action[4:]
        todos = read()
        todos.append(user_action + '\n')
        write(todos)

    elif user_action.startswith('show'):

        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos = read()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")
        print(f"We have {len(todos)} task in the list.")

    elif user_action.startswith('edit'):
        read()
        user_action = user_action[5:]
        if user_action.isnumeric():
            number = int(user_action)
            if len(todos) >= number > 0:
                todos[number - 1] = input("Enter new todo : ") + "\n"

            else:
                print(f"{number} is not present in the list.")
        else:
            flag = 0
            for index, item in enumerate(todos):
                if user_action in item:
                    todos[index] = (input("Enter new todo : ") + '\n')
                    flag = 1
            if flag == 0:
                print(f"{user_action} not present in the list.")
        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        write(todos)

    elif user_action.startswith('complete'):
        user_action = user_action[9:]
        todos = read()
        if user_action.isnumeric():
            number = int(user_action)
            if len(todos) >= number > 0:
                print("todo", todos[number - 1].strip('\n'), "is removed.")
                todos.pop(number - 1)
            else:
                print(f"{number} is not present in the list")

        else:
            for index, item in enumerate(todos):
                if user_action in item:
                    print("todo", user_action, "is removed.")
                    todos.pop(index)
                else:
                    print(f"{user_action} is not present in the list.")

        write(todos)

    elif user_action.startswith('exit'):
        break
    else:
        print("Wrong command entered !")

print("Thank You !!")
