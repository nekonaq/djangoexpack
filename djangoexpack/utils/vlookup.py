def vlookup(value, table, default=None):
    latest = default
    for el in table:
        if value == el[0]:
            return el[1]

        if value < el[0]:
            return latest
        latest = el[1]

    return latest
