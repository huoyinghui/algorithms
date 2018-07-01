class Slot(object):
    """定义一个 hash 表 数组的槽
    注意，一个槽有三种状态，看你能否想明白
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    def get(self, key, default):
        return

    def add(self, key, value):
        return

    def remove(self, key):
        return


inserted_index_set = set()
M = 10

def h(key, M=10):
    return key % M

to_insert = [1, 5, 9, 11, 2, 12]

def main():
    for number in to_insert:
        index = h(number)
        first_index = index
        i = 1
        while index in inserted_index_set:
            print('\th({number}) = {number} % M = {index} collision'.format(
                number=number, index=index))
            index = (first_index + i*i) % M
            i += 1
        else:
            print('h({number}) = {number} % M = {index}'.format(
                number=number, index=index))
            inserted_index_set.add(index)
    pass

if __name__ == '__main__':
    main()
    
