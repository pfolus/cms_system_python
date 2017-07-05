from employee_view imoprt *


def greet(user):

    print("Hello " + user.name + "!")


def print_menu():

    print('''1. List mentors
          2. List mentors with details
          3. Add mentor
          4. Remove mentor
          5. List students
          6. List students with details
          0. Log out
          ''')


def option_error():

    print("There isn't such option!")


def show_mentors_with_details(mentors):

    index = 1

    for mentor in mentors:
        print("{}. {} {} - {}".format(index, mentor.name,
                                      mentor.surname, mentor.login))
        index += 1


def show_mentors(mentors):

    index = 1

    for mentor in mentors:
        print("{}. {} {}".format(index, mentor.name, mentor.surname))
        index += 1
