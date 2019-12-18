def gcd(x, y):
    # Code taken from: https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def three_way_lcm(x, y, z):
    # Code taken from: https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
    return lcm(x, lcm(y, z))
