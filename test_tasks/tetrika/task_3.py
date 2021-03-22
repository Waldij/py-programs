import logging
import matplotlib.pyplot as plt
from exceptions import ConversionError, IntersectionError, TotalTimeError

logging.basicConfig(
    filename="debug/debug_task_3.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


def intersections(first_interval: list, second_interval: list) -> list:
    """
    Returns the intersection of two intervals
    :param first_interval:  [[start, end], [start, end], ....]
    :param second_interval: [[start, end], [start, end], ....]
    :return: intersection intervals
    """
    intersection_intervals = []
    first_interval_index = second_interval_index = 0
    while first_interval_index < len(first_interval) and second_interval_index < len(second_interval):
        """
        a_left-----a_right
        b_left-----b_right
        """
        a_left, a_right = first_interval[first_interval_index]
        b_left, b_right = second_interval[second_interval_index]

        if a_right < b_right:
            first_interval_index += 1
        else:
            second_interval_index += 1

        if a_right >= b_left and b_right >= a_left:
            end_pts = sorted([a_left, a_right, b_left, b_right])
            middle = [end_pts[1], end_pts[2]]
            intersection_intervals.append(middle)

    index = 0
    while index < len(intersection_intervals) - 1:
        if intersection_intervals[index][1] == intersection_intervals[index + 1][0]:
            intersection_intervals[index:index + 2] = [[intersection_intervals[index][0],
                                                        intersection_intervals[index + 1][1]]]
        index += 1

    return intersection_intervals


def find_all_intersections(*args):
    """
    Finds the intersection of all intervals in *args
    :param args: [[start, end], [start, end], ....], --//--
    :return: intersection intervals
    """
    result = args[0]
    for intervals in args:
        result = intersections(result, intervals)
    return result


def merge_intervals(intervals: list):
    """
    Merges overlapping intervals
    :param intervals: [[start, end], [start, end], ....]
    :return: merged intervals
    """
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged


def count_total_time(intervals: list) -> int:
    """
    Returns the total time by intervals.
    :param intervals: [[start, end], [start, end], ....]
    :return total time (int)
    """
    count = 0
    for interval in intervals:
        count += interval[1] - interval[0]
    return count


def pair_up(intervals: list, count: int = 2) -> list:
    """
    Returns paired intervals (default) or divided into parts by count
    :param intervals: [start, end, start, end, ...]
    :param count: divided into parts by count (int)
    :return paired interval [[start, end], [start, end], ....]
    """
    return list(list(x) for x in zip(*[iter(intervals)] * count))


def appearance(intervals: dict):
    """
    Returns the time of the general presence of the student and teacher in the lesson (in seconds)
    :param intervals: { 'lesson': [1594663200, 1594666800],
                        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
    :return: total time
    """
    try:
        lesson = pair_up(intervals['lesson'])
        pupil = merge_intervals(pair_up(intervals['pupil']))
        tutor = merge_intervals(pair_up(intervals['tutor']))
        logging.debug("Values:\n\tlesson:\t{}\n\tpupil:\t{}\n\ttutor:\t{}".format(lesson, pupil, tutor))
    except Exception as e:
        logging.debug(e)
        raise ConversionError(e)

    try:
        all_intersections = find_all_intersections(lesson, pupil, tutor)
        logging.debug("Values:\n\tall intersections:\t{}".format(all_intersections))
    except Exception as e:
        logging.debug(e)
        raise IntersectionError(e)

    try:
        total_time = count_total_time(all_intersections)
        logging.debug("Values:\n\ttotal time result:\t{}".format(total_time))
    except Exception as e:
        logging.debug(e)
        raise TotalTimeError(e)

    return total_time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    logging.debug("\nRunning program...")
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
