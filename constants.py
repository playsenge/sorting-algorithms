# List of algorithms
SORTING_ALGORITHMS: tuple = 'bubble_sort', 'insertion_sort', 'quick_sort', 'heap_sort', 'merge_sort', 'radix_sort', 'shell_sort'

# Constants
QUIT_DELAY: int = 500
ELEMENTS: int = 100
SCREEN_SIZE: tuple[int, int] = 1600, 900
BAR_WIDTH = SCREEN_SIZE[0] // ELEMENTS
MAX_BAR_HEIGHT = SCREEN_SIZE[1] - 20

# Dictionaries
FRAMERATES: dict[str, float] = {
    'bubble_sort': 600,
    'insertion_sort': 30,
    'shell_sort': 100,
    'quick_sort': 20,
    'heap_sort': 25,
    'merge_sort': 30,
    'radix_sort': 150,
}
COLORS: dict[str, tuple[int, int, int]] = {
    'black': (0, 0, 0),
    'green': (0, 255, 0),
    'white': (255, 255, 255),
}
