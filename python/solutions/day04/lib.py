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

    matching_pair = None
    last_pair = None
    for lh_val, rh_val in adjacent_pairs:
        # check non-decreasing
        if lh_val > rh_val:
            return False

        if lh_val == rh_val:
            if allow_matching_pairs_in_larger_group:
                matching_pair = lh_val, rh_val
            else:
                if matching_pair is None and last_pair != (lh_val, rh_val):
                    matching_pair = lh_val, rh_val
                elif matching_pair is not None and last_pair == matching_pair == (lh_val, rh_val):
                    matching_pair = None

        last_pair = lh_val, rh_val

    if matching_pair is None:
        return False

    return True


def get_pw_candidates(allow_matching_pairs_in_larger_group):
    return [num for num in range(MIN_INPUT, MAX_INPUT + 1) if _is_candidate(num, allow_matching_pairs_in_larger_group)]
