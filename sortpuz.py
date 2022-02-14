import argparse
import copy
import time
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class PlayField:
    formation: List[List[str]]
    moves: List[Tuple[int, int]]


def is_column_fully_sorted(column, max_column_length):
    """Check if a column is fully sorted, that is, if it's empty or full of the same colour

    >>> is_column_fully_sorted(['b', 'b', 'b', 'b'], 4)
    True
    >>> is_column_fully_sorted([], 4)
    True
    >>> is_column_fully_sorted(['b', 'b', 'b', 'o'], 4)
    False
    >>> is_column_fully_sorted(['b', 'b', 'b'], 4)
    False

    :param column: list to check sorted status
    :param max_column_length: length of a full column
    :returns: whether the column is fully sorted
    """
    return len(column) == 0 or column.count(column[0]) == max_column_length


def is_formation_sorted(formation, max_column_length):
    """Check if a formation is fully sorted

    >>> is_formation_sorted([['b', 'b', 'b', 'b'], []], 4)
    True
    >>> is_formation_sorted([['b', 'b', 'b'], ['o']], 4)
    False

    :param formation: formation to check sorted status
    :param max_column_length: length of a full column
    :returns: whether the formation is fully sorted
    """
    is_sorted = True

    for column in formation:
        if not is_column_fully_sorted(column, max_column_length):
            is_sorted = False
            break

    return is_sorted


def get_next_formations(formation, past_moves, max_column_length):
    """Get the next possible formations that can be formed from the passed formation

    >>> get_next_formations([['b', 'b'], ['b', 'b']], [], 4)
    ([[[], ['b', 'b', 'b', 'b']], [['b', 'b', 'b', 'b'], []]], [[(1, 2)], [(2, 1)]])

    :param formation: formation whose next possible formations are being sought
    :param past_moves: moves that have led to the current formation
    :param max_column_length: length of a full column
    :returns: next possible formations, and their respective moves
    """
    formations = []
    moves = []

    for i, list_i in enumerate(formation):
        if is_column_fully_sorted(list_i, max_column_length):
            continue

        list_i_length = len(list_i)
        halfway_level = max_column_length // 2 + 1
        is_list_i_sorted = list_i_length == list_i.count(list_i[0])
        is_list_i_over_halfway_full = list_i_length >= halfway_level
        move_to_empty_column_made = False

        if is_list_i_sorted and is_list_i_over_halfway_full:
            continue

        for j, list_j in enumerate(formation):
            list_j_length = len(list_j)
            valueless_moves = [
                i == j,
                is_list_i_sorted and list_j_length == 0,
                move_to_empty_column_made and list_j_length == 0
            ]
            is_move_possible = list_j_length == 0 or list_j_length < max_column_length and list_i[-1] == list_j[-1]

            if any(valueless_moves) or not is_move_possible:
                continue

            if list_j_length == 0:
                move_to_empty_column_made = True

            next_move = (i + 1, j + 1)
            previous_move = past_moves[-1] if len(past_moves) > 1 else None
            formation_copy = copy.deepcopy(formation)

            formation_copy[j].append(formation_copy[i].pop())

            while len(formation_copy[i]) > 0 and len(formation_copy[j]) < 4:
                if formation_copy[i][-1] != formation_copy[j][-1]:
                    break
                formation_copy[j].append(formation_copy[i].pop())

            if len(formation_copy[i]) > 0 and formation_copy[i][-1] == formation_copy[j][-1]:
                continue

            if previous_move and (previous_move[1], previous_move[0]) == next_move:
                moves.append(past_moves[:-1] + [next_move])
            else:
                moves.append(past_moves + [next_move])

            formations.append(formation_copy)

    return formations, moves


def show_progress(start_time, counter, progress_format="{counter} formations visited in {h:02d}:{m:02d}:{s:02d}"):
    """Show progress of a task whose completion time is unkown

    :param start_time: time the task began
    :param counter: number that shows progress of the task
    :param progress_format: format of the progress display
    """
    time_taken = time.time() - start_time
    minutes, seconds = divmod(time_taken, 60)
    hours, _ = divmod(minutes, 60)
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)

    print(progress_format.format(counter=counter, h=hours, m=minutes, s=seconds), end="\r")


def breadth_first_search(formation, max_column_length, verbose):
    """Perform a breadth first search for an optimal solution

    >>> breadth_first_search([['b', 'b'], ['b', 'b']], 4, False)
    ([[], ['b', 'b', 'b', 'b']], [(1, 2)])

    :param formation: formation whose solution is being sought
    :param max_column_length: length of a full column
    :param verbose: whether to display progress
    :returns: a sorted formation, and moves that led to this formation
    """
    play_fields = [PlayField(formation, [])]
    moves_result = None
    formation_result = None
    visited_formations = [formation]
    counter = 1
    start_time = time.time()

    if is_formation_sorted(formation, max_column_length):
        show_progress(start_time, counter)
        moves_result = []
        formation_result = formation

    while moves_result is None and len(play_fields) > 0:
        replacement_play_fields = []

        for play_field in play_fields:
            to_break = False
            next_formations, next_moves = get_next_formations(play_field.formation, play_field.moves, max_column_length)

            for next_formation, next_move in zip(next_formations, next_moves):
                if set([tuple(i) for i in next_formation]) in visited_formations:
                    continue

                if verbose:
                    counter += 1
                    show_progress(start_time, counter)

                if is_formation_sorted(next_formation, max_column_length):
                    moves_result = next_move
                    formation_result = next_formation
                    to_break = True
                    break

                visited_formations.append(set([tuple(i) for i in next_formation]))
                replacement_play_fields.append(PlayField(next_formation, next_move))

            if to_break:
                break

        play_fields = replacement_play_fields

    if verbose:
        print()

    return formation_result, moves_result


def depth_first_search(formation, max_column_length, verbose):
    """Perform a depth first search for a solution that's encountered first

    >>> depth_first_search([['b', 'b'], ['b', 'b']], 4, False)
    ([[], ['b', 'b', 'b', 'b']], [(1, 2)])

    :param formation: formation whose solution is being sought
    :param max_column_length: length of a full column
    :param verbose: whether to display progress
    :returns: a sorted formation, and moves that led to this formation
    """
    play_fields = [PlayField(formation, [])]
    moves_result = None
    formation_result = None
    visited_formations = []
    counter = 0
    start_time = time.time()

    while len(play_fields) > 0:
        if verbose:
            counter += 1
            show_progress(start_time, counter)

        play_field = play_fields.pop(0)
        visited_formations.append(set([tuple(i) for i in play_field.formation]))

        if is_formation_sorted(play_field.formation, max_column_length):
            moves_result = play_field.moves
            formation_result = play_field.formation
            break

        next_formations, next_moves = get_next_formations(play_field.formation, play_field.moves, max_column_length)
        play_fields_to_prepend = []

        for next_formation, next_move in zip(next_formations, next_moves):
            if set([tuple(i) for i in next_formation]) not in visited_formations:
                play_fields_to_prepend.append(PlayField(next_formation, next_move))

        play_fields = play_fields_to_prepend + play_fields

    if verbose:
        print()

    return formation_result, moves_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-q", "--quick", default=False, action="store_true",
        help="Whether to use depth first search, which most of the time is quicker, though the resultant solution may "
             "not be optimal. The default is breadth first search, which is guaranteed to provide an optimal solution, "
             "though is slower most of the time."
    )
    parser.add_argument("-hp", "--hide-progress", default=True, action="store_false", help="Whether to hide progress")
    parser.add_argument("-l", "--length", type=int, default=4, help="Length of a full column")
    parser.add_argument("formation", metavar="FORMATION", type=str, nargs="+", help="Arrangement of the colour columns")

    args = parser.parse_args()
    formation_passed = []

    for a_column in args.formation:
        if a_column[0] != "+":
            formation_passed.append(a_column.split(","))
        else:
            formation_passed.append([])

    [print(a_column) for a_column in formation_passed]

    if args.quick:
        sorted_formation, sorted_moves = depth_first_search(formation_passed, args.length, args.hide_progress)
    else:
        sorted_formation, sorted_moves = breadth_first_search(formation_passed, args.length, args.hide_progress)

    if sorted_formation:
        len_of_sorted_moves = len(sorted_moves)
        print(f"{len_of_sorted_moves} {'move' if len_of_sorted_moves == 1 else 'moves'}")
        [print(a_column) for a_column in sorted_formation]
        [print(a_move) for a_move in sorted_moves]
    else:
        print("No sorted formation found")
