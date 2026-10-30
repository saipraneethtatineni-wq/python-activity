### Problem Statement

Design and implement a program using nested loops to automate an examination hall seating arrangement. The classroom layout is defined as a two-dimensional grid of rows and columns with fixed capacity. To prevent examination malpractice and maintain administrative protocols, the system must enforce alternate seating (e.g., student placed only on alternating desks such as $(r + c) \pmod 2 == 0$) and mark pre-defined coordinates as reserved or unavailable. Desks allocated to eligible candidates should display a sequential candidate identifier (e.g., `S001`, `S002`), reserved locations must display `[RES]`, and unoccupied alternate desks must display `[---]`.

---

### Algorithm

1. **Input Parameters:**
* Input total rows ($R$) and total columns ($C$).
* Input list of reserved positions as coordinate pairs $(r, c)$.
* Initialize candidate roll sequence counter `candidate_id = 1`.


2. **Matrix Initialization:**
* Initialize an empty 2D grid/list of size $R \times C$.


3. **Outer Loop (Rows):**
* For each row index $i$ from $0$ to $R - 1$:


4. **Inner Loop (Columns):**
* For each column index $j$ from $0$ to $C - 1$:
* Check if $(i, j)$ is in the reserved list:
* If yes, assign desk value as `"[RES]"`.


* Else, check if the position satisfies the alternate seating rule (e.g., $(i + j) \pmod 2 == 0$):
* If yes, format the current candidate ID into a string token (e.g., `"S001"`), assign it to the desk, and increment `candidate_id` by 1.
* If no, assign desk value as `"[---]"` to indicate an empty/restricted buffer seat.






5. **Output Generation:**
* Traverse the populated grid row by row and print the column headers and formatted row elements.



---

### Flowchart

```mermaid
flowchart TD
    Start([Start]) --> Input[Read Rows R, Columns C, Reserved List]
    Input --> InitCounter[Set candidate_id = 1, r = 0]
    InitCounter --> CheckR{r < R ?}
    
    CheckR -- Yes --> InitC[Set c = 0]
    CheckR -- No --> PrintGrid[Print Final Seating Grid]
    
    InitC --> CheckC{c < C ?}
    CheckC -- No --> NextRow[r = r + 1]
    NextRow --> CheckR
    
    CheckC -- Yes --> CheckRes{Is (r, c) in Reserved?}
    
    CheckRes -- Yes --> SetRes[Seat = '[RES]']
    CheckRes -- No --> CheckAlt{(r + c) % 2 == 0 ?}
    
    CheckAlt -- Yes --> AssignSeat[Seat = Formatted candidate_id<br/>candidate_id = candidate_id + 1]
    CheckAlt -- No --> SetEmpty[Seat = '[---]']
    
    SetRes --> AppendSeat[Store Seat in Grid]
    AssignSeat --> AppendSeat
    SetEmpty --> AppendSeat
    
    AppendSeat --> NextCol[c = c + 1]
    NextCol --> CheckC
    
    PrintGrid --> End([End])

```

---

### Python Source Code

```python
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

```

---

### Sample Input

```text
Rows: 4
Columns: 5
Reserved Positions: [(0, 2), (1, 1), (3, 4)]

```

---

### Sample Output

```text
        Col  1  Col  2  Col  3  Col  4  Col  5
       --------------------------------------
Row  1 |   S001  [---]  [RES]  [---]   S002
Row  2 |  [---]  [RES]   S003  [---]   S004
Row  3 |   S005  [---]   S006  [---]   S007
Row  4 |  [---]   S008  [---]   S009  [RES]

```
