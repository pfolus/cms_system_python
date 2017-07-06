import getpass

def wrong_user():
    print("\nThere isn't such user\n")


def show_login_menu():

    print("""
    ===== Welcome to =====
    ======Canvas 1.0======
    """)


def get_login():

    return input("Please provide an username: ")


def get_password():

    return getpass.getpass("Please provide a password: ")
