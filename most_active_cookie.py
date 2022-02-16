import sys


"""
    Returns the most cookie with the most activity.
    >>> most_active_cookie(2018-12-09)
    AtY0laUfhglK3lC7
    >>> most_active_cookie(2018-12-09)
    SAZuXPGUrfbcn5UA
    4sMM2LxV07bPJzwf
    fbcn5UAVanZf6UtG
    >>> most_active_cookie(2018-12-07)
    4sMM2LxV07bPJzwf
"""

def most_active_cookie(selected_date):
    with open('cookies.txt') as f:
        lines = f.readlines()

    cookie_activity_map = {}

    for line in lines:
        cookie = line.split(',')
        key = cookie[0]
        date = cookie[1][:10]
        if date == selected_date:
            if key not in cookie_activity_map:
                cookie_activity_map[key] = 0
            cookie_activity_map[key] += 1

    top_keys = set()
    max_key = 0
    for keys in cookie_activity_map:
        count = cookie_activity_map[keys]
        if count > max_key:
            max_key = count
            top_keys.clear()
            top_keys.add(keys)
        if count == max:
            top_keys.add(keys)

    for result in top_keys:
        print(result)


def main():
    args = sys.argv[1:][2]
    most_active_cookie(args)


if __name__ == '__main__':
    main()
