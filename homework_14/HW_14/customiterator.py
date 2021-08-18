class CustomIterator:
    def __init__(self,  sequence, start_index, end_index):
        self.__sequence = sequence
        self.__end_index = end_index
        self.__current_item = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_item < self.__end_index:
            seq_item = self.__sequence[self.__current_item]
            self.__current_item += 1
            return seq_item
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator_sample = CustomIterator('super iterator', 0, 3)
    for item in iterator_sample:
        print(item)

# Nice good work
