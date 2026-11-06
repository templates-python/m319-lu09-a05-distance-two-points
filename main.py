"""Calculates the distance between two points in the CH1903 coordinate system."""


def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points in CH1903 coordinate system.
    :param x1: X coordinate of the first point.
    :param y1: Y coordinate of the first point.
    :param x2: X coordinate of the second point.
    :param y2: Y coordinate of the second point.
    :return: float - the distance between the two points.
    """
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    distance /= 1000
    return distance


def main():
    """
    Asks the user for the coordinates of two points and prints the distance between them.
    :return: None
    """
    print('Bitte geben Sie die Koordinaten des ersten Punktes ein (x1, y1):')
    x1 = float(input('x1: '))
    y1 = float(input('y1: '))
    print('Bitte geben Sie die Koordinaten des zweiten Punktes ein (x2, y2):')
    x2 = float(input('x2: '))
    y2 = float(input('y2: '))

    distance = calculate_distance(x1, y1, x2, y2)
    print(f'Die Distanz zwischen den beiden Punkten beträgt: {distance} km')


if __name__ == '__main__':
    main()
