def part_1(input_file: str) -> int:
    grid = []
    with open(input_file) as f:
        grid.extend([x.strip() for x in f.readlines()])

    # from a point, go to 8 direction (surrounding)
    # (x, y) : x is row, y is column
    directions = [
        (0, 1),  # → right: 0 = same row, +1 = move one column to the right
        (0, -1),  # ← left: 0 = same row, -1 = move one column to the left
        (1, 0),  # ↓ down: +1 = move down one row, 0 = same column
        (-1, 0),  # ↑ up: -1 = move up one row, 0 = same column
        (1, 1),  # ↘ down-right: +1 = move down one row, +1 = move one column to the right
        (1, -1),  # ↙ down-left: +1 = move down one row, -1 = move one column to the left
        (-1, -1),  # ↖ up-left: -1 = move up one row, -1 = move one column to the left
        (-1, 1),  # ↗ up-right: -1 = move up one row, +1 = move one column to the right
    ]

    rows: int = len(grid)
    cols: int = len(grid[0])
    word: str = "XMAS"
    word_len: int = len(word)

    def is_valid(x, y):
        """Check if a position is within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(row: int, col: int, row_direction: int, col_direction: int) -> bool:
        for k in range(word_len):
            nr, nc = row + k * row_direction, col + k * col_direction
            if not is_valid(nr, nc) or grid[nr][nc] != word[k]:
                return False
        return True

    count = 0
    for row in range(rows):  # for each row
        for col in range(cols):  # for  each column
            for dr, dc in directions:
                if check_direction(row, col, dr, dc):
                    count += 1
    return count


def test_part_1():
    assert part_1("day_04/sample.txt") == 18
    print(f'\nPart 1 {part_1("day_04/data.txt")}')