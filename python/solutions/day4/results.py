"""Problem URL: https://adventofcode.com/2019/day/4"""


from .lib import get_pw_candidates


if __name__ == '__main__':
    print(f'Part 1:  {len(get_pw_candidates(True))}')
    print(f'Part 2:  {len(get_pw_candidates(False))}')
