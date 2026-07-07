current_user = None


def create_session(user):

    global current_user

    current_user = user


def get_current_user():

    return current_user


def destroy_session():

    global current_user

    current_user = None