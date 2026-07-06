from database import (
    get_total_contacts,
    get_today_contacts
)


def dashboard_statistics():

    return {
    "total_contacts": get_total_contacts(),
    "today_contacts": get_today_contacts()
}