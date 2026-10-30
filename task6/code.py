def generate_seating(rows, cols, reserved_coords):
    grid = []
    candidate_id = 1
    reserved_set = set(reserved_coords)

    for r in range(rows):
        row_seats = []
        for c in range(cols):
            if (r, c) in reserved_set:
                row_seats.append("[RES]")
            elif (r + c) % 2 == 0:
                row_seats.append(f"S{candidate_id:03d}")
                candidate_id += 1
            else:
                row_seats.append("[---]")
        grid.append(row_seats)

    return grid


def display_seating(grid):
    cols = len(grid[0])
    header = "       " + " ".join([f"Col {c+1:>2}" for c in range(cols)])
    print(header)
    print("       " + "-" * (cols * 7 - 1))
    for r_idx, row in enumerate(grid):
        row_str = f"Row {r_idx+1:>2} | " + " ".join([f"{seat:>6}" for seat in row])
        print(row_str)


if __name__ == "__main__":
    R = 4
    C = 5
    reserved = [(0, 2), (1, 1), (3, 4)]

    seating_plan = generate_seating(R, C, reserved)
    display_seating(seating_plan)
