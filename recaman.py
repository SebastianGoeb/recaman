import bisect


def recaman(start=0, step_increment=1, first_step=1):
    current = start
    step = first_step
    visited = [0]
    yield (current)

    while True:
        backward_candidate = current - step
        already_visited = visited[bisect.bisect_left(visited, backward_candidate)] == backward_candidate
        if backward_candidate < 0 or already_visited:
            current = current + step
        else:
            current = current - step
        step = step + step_increment
        bisect.insort(visited, current)
        yield (current)
