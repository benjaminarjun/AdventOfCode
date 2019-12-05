MIN_INPUT = 256310
MAX_INPUT = 732736


def _is_candidate(num, allow_matching_pairs_in_larger_group, enforce_puzzle_input_range = True):
    # 6 digits
    if num < 100000 or num > 999999:
        return False

    # between min and max
    if enforce_puzzle_input_range and (num < MIN_INPUT or num > MAX_INPUT):
        return False

    # two adjacent matching
    digits = [int(digit) for digit in list(str(num))]
    adjacent_pairs = zip(digits, digits[1:])

    has_matching_pair = False
    last_pair = None
    for lh_val, rh_val in adjacent_pairs:
        # check non-decreasing
        if lh_val > rh_val:
            return False

        if lh_val == rh_val:
            if not allow_matching_pairs_in_larger_group and last_pair == (lh_val, rh_val):
                has_matching_pair = False
            else:
                has_matching_pair = True

        last_pair = lh_val, rh_val

    if not has_matching_pair:
        return False

    return True


def get_pw_candidates(allow_multiple_matching_pairs):
    return [num for num in range(MIN_INPUT, MAX_INPUT + 1) if _is_candidate(num, allow_multiple_matching_pairs)]
