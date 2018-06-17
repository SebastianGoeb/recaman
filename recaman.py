def recaman(iterations, start=0, step_increment=1, first_step=1):
    current = start
    step = first_step
    visited = []
    while len(visited) < iterations:
        backward_candidate = current - step
        if backward_candidate <= 0 or backward_candidate in visited:
            current = current + step
        else:
            current = current - step
        step = step + step_increment
        visited.append(current)
        yield (current)
