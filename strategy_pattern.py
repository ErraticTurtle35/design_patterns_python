from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def _sort(self, list_to_sort):
        pass

    def sort(self, list_to_sort):
        return self._sort(list_to_sort)


class DeepSort(SortingStrategy):
    def _sort(self, list_to_sort):
        print("DeepSort")
        return list_to_sort


class BubbleSort(SortingStrategy):
    def _sort(self, list_to_sort):
        print("BubbleSort")
        return list_to_sort


class MergeSort(SortingStrategy):
    def _sort(self, list_to_sort):
        print("MergeSort")
        return list_to_sort


# -------------------------------------------------

SORTING_STRATEGIES = {
    'bubble': BubbleSort,
    'merge': MergeSort,
    'deep': DeepSort
}


class Client:
    def __init__(self):
        self.random_list = [1, 4, 2, 64, 2]

    def sorting_random_list(self, strategy_to_use):
        sorted_random_list = SORTING_STRATEGIES[strategy_to_use]().sort(self.random_list)
        print("SORTED: {}".format(sorted_random_list))


newClient = Client()
newClient.sorting_random_list('bubble')
newClient.sorting_random_list('merge')
newClient.sorting_random_list('deep')
