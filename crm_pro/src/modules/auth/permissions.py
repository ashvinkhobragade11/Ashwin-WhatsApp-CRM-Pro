from modules.auth.session_manager import get_current_user


def get_current_role():

    user = get_current_user()

    if user is None:
        return None

    return user[2]


def is_admin():

    return get_current_role() == "Admin"


def is_manager():

    return get_current_role() == "Manager"


def is_executive():

    return get_current_role() == "Executive"

def can_view_users():

    return is_admin() or is_manager()

def can_manage_users():

    return is_admin()