def run():
    from math import sqrt
    # cubes = {}
    # for i in range(1, 101):
    #     cubes[i] = i**3

    # cubes = {i: i**3 for i in range(1, 101)}

    # cubes = {}
    # for i in range(1, 101):
    #     if i%3 != 0:
    #         cubes[i] = i**3

    # cubes = {i:i**3 for i in range(1, 101) if i%3 !=0}

    # cubes = {i: round(i**(1/2), 2) for i in range(1, 9999) if i%3 !=0}

    cubes = {i: round(sqrt(i),2) for i in range(1, 9999) if i%3 !=0}

    print(cubes)

if __name__ == '__main__':
    run()