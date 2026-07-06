activities = []


def add_activity(action):

    activities.insert(
        0,
        action
    )

    if len(activities) > 20:
        activities.pop()


def get_recent_activities():

    return activities