import sys


"""
    Returns the most cookie with the most activity.
    Below are tests.
    >>> most_active_cookie(2018-12-09)
    AtY0laUfhglK3lC7
    >>> most_active_cookie(2018-12-09)
    SAZuXPGUrfbcn5UA
    4sMM2LxV07bPJzwf
    fbcn5UAVanZf6UtG
    >>> most_active_cookie(2018-12-07)
    4sMM2LxV07bPJzwf
"""

"""
Primary Function.
Returns the most active cookies. If there are multiple cookies that are tied, all of those cookies will be printed as well on new lines.
"""
def most_active_cookie(selected_date):
    with open('cookies.txt') as f: # Reads the file.
        lines = f.readlines() 

    cookie_activity_map = {} # Map all of cookies accessed that day. The value is the number of occurences.

    for line in lines: # Loops through each line in the document.
        cookie = line.split(',') # Splits the key and date into to elements.
        key = cookie[0]
        date = cookie[1][:10] # date is the year, month, and day. We do not care about the time.
        if date == selected_date: # the date of the cookie matches the date that we have selected.
            if key not in cookie_activity_map: # The map is updated.
                cookie_activity_map[key] = 0
            cookie_activity_map[key] += 1

    top_keys = set() # Set of all top keys. A set is used to ensure no cookies are repeated.
    max_key = 0
    for keys in cookie_activity_map: # Finds the top keys. Adds it to the map.
        count = cookie_activity_map[keys]
        if count > max_key:
            max_key = count
            top_keys.clear()
            top_keys.add(keys)
        if count == max:
            top_keys.add(keys)

    for result in top_keys: # Prints all the top cookies line by line.
        print(result)


def main():
    args = sys.argv[1:][2] # An example command input would be "most_active_cookie.py cookie_log.csv -d 2018-12-08".
    most_active_cookie(args)


if __name__ == '__main__':
    main()
