from database import get_total_contacts


def dashboard_statistics():

    return {
        "total_contacts": get_total_contacts()
    }