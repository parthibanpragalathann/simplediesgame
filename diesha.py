# The Game of Diesha
# Initialise target scores
target_val = 10
# Initialise player scores in list
a_list = []
b_list = []
# Initialise player scores
current_a = 0
current_b = 0
# Initialise player choice
choice = [1, 2, 3, 4, 5, 6]
# Initialise iter  player scores for validation
add_iter_value_a = 0
add_iter_value_b = 0
# Selection A: based on comparison of the Player A value
def check_a_value(a, add_iter_value_a):
    # Repeat everything in this list of a
    for iter_value in a_list:
        add_iter_value_a += iter_value
    # Display the Iter A values
    print("Iter A value of ", add_iter_value_a)
    #check a value
    checked_a = add_iter_value_a + a
    if checked_a <= target_val:
        # Display the A value when touch target
        print("your input A is valid")
        n = a
    else:
        n = 0
        print("your input A is invalid")
    return n
# Selection B: based on comparison of the Player B value
def check_b_value(b, add_iter_value_b):
    # Repeat everything in this list of b
    for iter_value in b_list:
        add_iter_value_b += iter_value
    print("Iter B value of ", add_iter_value_b)
    #check b value
    checked_b = add_iter_value_b + b
    if checked_b <= target_val:
        print("your input B is valid")
        n = b
    else:
        n = 0
        print("your input B is invalid")
    return n


def get_a(current_a, add_iter_value_a):
    #Get input player A value
    a = int(input("Player A please Enter the A value : "))
    print("Now Enter Player A of point : ", a)
    #valid player A value is less then or equal to target value
    valid_val = check_a_value(a, add_iter_value_a)
    #check value in choice and valid
    if a in choice and valid_val != 0:
        #add a value in the list a
        a_list.append(a)
        print("list of A is ", a_list)
        #iter a value to calculate for hit the target or not to try
        for iter_a in a_list:
            current_a += iter_a
        print("Now  player A Current point is :", current_a)
        #valid a value achive or not
        if target_val == current_a:
            # Display the A value when touch target
            print("Player A win the GAME ! ")
        else:
            #call b for get inputs in Player B
            get_b(current_b, add_iter_value_b)
    else:
        #invalid input so again get Player a value
        print("Player A your Current point is invalid try again !\n")
        get_a(current_a, add_iter_value_a)


def get_b(current_b, add_iter_value_b):
    # Get input player B value
    b = int(input("Player B please Enter the B value : "))
    print("Now Enter Player B of point : ", b)
    # valid player B value is less then or equal to target value
    valid_val = check_b_value(b, add_iter_value_b)
    # valid player B value is less then or equal to target value
    if b in choice and valid_val != 0:
        b_list.append(b)
        print("list of B is ", b_list)
        # iter b value to calculate for hit the target or not to try
        for iter_b in b_list:
            current_b += iter_b
        print("Now  player B Current point is :", current_b)
        # valid b value achive or not
        if target_val == current_b:
            # Display the B value when touch target
            print("Player B win the GAME ! ")
        else:
            #call a for get inputs in Player A
            get_a(current_a, add_iter_value_a)
    else:
        #invalid input so again get Player b value
        print("Player B your Current point is invalid try again !\n")
        get_b(current_b, add_iter_value_b)

#main function of The Game Diesha
if __name__ == "__main__":
    #Display when Game start
    print("Game start Now !")
    #Display The Game Choice
    print("Your Choice is  ", choice)
    get_a(current_a, add_iter_value_a)


