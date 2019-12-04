"""Problem URL: https://adventofcode.com/2019/day/4"""


MIN_INPUT = 256310
MAX_INPUT = 732736


def _is_candidate(num):
    # 6 digits
    if num < 100000 or num > 999999:
        return False

    # between min and max
    if num < MIN_INPUT or num > MAX_INPUT:
        return False

    # two adjacent matching
    digits = [int(digit) for digit in list(str(num))]
    adjacent_pairs = zip(digits, digits[1:])

    has_adjacent_matching = False
    for lh_val, rh_val in adjacent_pairs:
        # check non-decreasing
        if lh_val > rh_val:
            return False
        if lh_val == rh_val:
            has_adjacent_matching = True

    if not has_adjacent_matching:
        return False
    
    return True


def get_pw_candidates():
    return [num for num in range(MIN_INPUT, MAX_INPUT + 1) if _is_candidate(num)]


if __name__ == '__main__':
    print(f'Part 1:  {len(get_pw_candidates())}')
