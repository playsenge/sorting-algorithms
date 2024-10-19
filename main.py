import pygame
import sorting
from constants import *
from sortable_array import SortableArray
from collections.abc import Generator

pygame.init()

screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Sorting algorithms!')

clock: pygame.time.Clock = pygame.time.Clock()

# Create a sortable array with elements from 1 to ELEMENTS
array: SortableArray = SortableArray(
    array=list(range(1, ELEMENTS + 1)),
    shuffle=True
)

array_max: int = max(array)  # Maximum value in the array for scaling

selected_algorithm_index: int = 0
running: bool = True


def get_sorting_generator(algorithm_name: str) -> Generator:
    """Returns the generator for the specified sorting algorithm."""
    match algorithm_name:
        case 'bubble_sort':
            return sorting.bubble_sort(array)
        case 'insertion_sort':
            return sorting.insertion_sort(array)
        case 'quick_sort':
            return sorting.quick_sort(array)
        case 'heap_sort':
            return sorting.heap_sort(array)
        case 'merge_sort':
            return sorting.merge_sort(array)
        case 'radix_sort':
            return sorting.radix_sort(array)
        case 'shell_sort':
            return sorting.shell_sort(array)
        case _:
            raise NotImplementedError(
                f'Sorting algorithm {repr(algorithm_name)} not available')


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    selected_algorithm_index -= 1
                    selected_algorithm_index %= len(SORTING_ALGORITHMS)

                case pygame.K_DOWN:
                    selected_algorithm_index += 1
                    selected_algorithm_index %= len(SORTING_ALGORITHMS)

                case pygame.K_RETURN:
                    sorting_generator: Generator = get_sorting_generator(
                        SORTING_ALGORITHMS[selected_algorithm_index])

                    while running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                        try:
                            next(sorting_generator)
                        except StopIteration:
                            running = False

                            pygame.time.delay(QUIT_DELAY)
                            pygame.quit()

                            break

                        screen.fill(COLORS['black'])

                        for i, element in enumerate(array):
                            bar_height = (element / array_max) * MAX_BAR_HEIGHT
                            x_pos = i * BAR_WIDTH
                            y_pos = SCREEN_SIZE[1] - bar_height
                            pygame.draw.rect(
                                screen, COLORS['green'], (x_pos, y_pos, BAR_WIDTH - 5, bar_height))

                        font: pygame.font.Font = pygame.font.SysFont(None, 36)
                        text_surface: pygame.Surface = font.render(
                            SORTING_ALGORITHMS[selected_algorithm_index], True, COLORS['green'])
                        screen.blit(text_surface, (10, 10))
                        pygame.display.update()
                        clock.tick(FRAMERATES.get(
                            SORTING_ALGORITHMS[selected_algorithm_index], 120))

    # Don't draw menu if algorithm finished
    if not running:
        break

    # Main menu
    screen.fill(COLORS['black'])
    menu_font: pygame.font.Font = pygame.font.SysFont(None, 36)
    for index, algorithm in enumerate(SORTING_ALGORITHMS):
        color = COLORS['green'] if index == selected_algorithm_index else COLORS['white']
        menu_text_surface: pygame.Surface = menu_font.render(
            algorithm, True, color)
        screen.blit(menu_text_surface, (10, 10 + index * 30))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
