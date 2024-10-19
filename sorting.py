from sortable_array import SortableArray
from collections.abc import Generator


def noop() -> Generator[None, None, None]:
    yield


def bubble_sort(array: SortableArray) -> Generator[None, None, None]:
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array.swap((j, j + 1))
            yield


def insertion_sort(array: SortableArray) -> Generator[None, None, None]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        yield


def quick_sort(array: SortableArray) -> Generator[None, None, None]:
    stack = [(0, len(array) - 1)]  # Start with the whole array on the stack

    while stack:
        low, high = stack.pop()  # Get the current subarray bounds
        if low >= high:
            continue

        pivot = array[(low + high) // 2]
        i, j = low, high

        while i <= j:
            # Move i to the right until finding an element >= pivot
            while array[i] < pivot:
                i += 1
            # Move j to the left until finding an element <= pivot
            while array[j] > pivot:
                j -= 1

            # Swap elements at i and j if i <= j
            if i <= j:
                array.swap((i, j))
                i += 1
                j -= 1
                yield  # Yield to allow the caller to pause

        # Push both subarrays onto the stack for further sorting
        if low < j:
            stack.append((low, j))  # Left half
        if i < high:
            stack.append((i, high))  # Right half


def heap_sort(array: SortableArray) -> Generator[None, None, None]:
    n = len(array)

    def heapify(end: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < end and array[left] > array[largest]:
            largest = left
        if right < end and array[right] > array[largest]:
            largest = right
        if largest != i:
            array.swap((i, largest))
            heapify(end, largest)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
        yield

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        array.swap((0, i))  # Move current root to end
        heapify(i, 0)
        yield


def merge_sort(array: SortableArray) -> Generator[None, None, None]:
    def merge(left: int, mid: int, right: int) -> Generator:
        left_half = array[left:mid + 1]
        right_half = array[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
            yield

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            yield

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
            yield

    def sort(left: int, right: int) -> Generator:
        if left < right:
            mid = (left + right) // 2
            yield from sort(left, mid)
            yield from sort(mid + 1, right)
            yield from merge(left, mid, right)

    yield from sort(0, len(array) - 1)


def radix_sort(array: SortableArray) -> Generator[None, None, None]:
    def sort(array: SortableArray, exp: int) -> Generator[None, None, None]:
        n = len(array)
        output = [0] * n
        count = [0] * 10  # Base 10

        for i in range(n):
            index = array[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = array[i] // exp
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            yield

        for i in range(n):
            array[i] = output[i]
            yield

    max_value = max(array)
    exp = 1

    while max_value // exp > 0:
        yield from sort(array, exp)
        exp *= 10


def shell_sort(array: SortableArray) -> Generator[None, None, None]:
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
                yield
            array[j] = temp
            yield
        gap //= 2
