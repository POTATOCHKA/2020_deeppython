import logging
import cProfile

logging.basicConfig(filename='logs.txt', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(message)s')


def check_aviable(arr):
    if isinstance(arr, list) or isinstance(arr, tuple):
        for i in arr:
            if not (isinstance(i, int) or isinstance(i, float)):
                logging.error('unaviable type')
                raise TypeError
    else:
        raise TypeError


def multiply(arr):
    check_aviable(arr)
    logging.debug('using multiply')
    new_arr = [1 for i in range(len(arr))]
    i, j = 0, (len(arr) - 1)
    left_half_multiply = 1
    right_half_multiply = 1
    while i < (len(arr) - 1) or (j > 0):
        left_half_multiply *= arr[i]
        right_half_multiply *= arr[j]
        new_arr[i + 1] *= left_half_multiply
        new_arr[j - 1] *= right_half_multiply
        i += 1
        j -= 1
    if isinstance(arr, tuple):
        logging.debug('using multiply with tuple')
        return tuple(new_arr)
    logging.debug('using multiply with list')
    return new_arr


if __name__ == '__main__':
    print(multiply((1,)))
    cProfile.run('multiply(list(range(1, 800)))', sort='tottime')
