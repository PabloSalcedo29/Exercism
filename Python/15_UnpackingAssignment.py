"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_id):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_id)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    x, y, z, *rest = each_wagons_id
    full_list = [z, *missing_wagons, *rest, x, y]
    return full_list


def add_missing_stops(dict_routes, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stop_list = []
    for number, name in stops.items():
        stop_list.append(name)
    dict_routes["stops"] = stop_list
    return dict_routes


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    for key, value in more_route_information.items():
        route[key] = value
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [*c1], [*c2], [*c3] = zip(*wagons_rows)
    return [c1, c2, c3]
