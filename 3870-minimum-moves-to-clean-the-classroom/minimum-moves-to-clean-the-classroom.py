class Solution(object):
    def minMoves(self, classroom, energy):
        """:type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        from collections import deque

        m = len(classroom)
        n = len(classroom[0])

        sr, sc = -1, -1
        litters = []
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))

        num_litters = len(litters)
        full_mask = (1 << num_litters) - 1
        litter_map = {pos: i for i, pos in enumerate(litters)}

        queue = deque()
        best_energy = {}

        initial_mask = 0
        queue.append((sr, sc, initial_mask, energy, 0))
        best_energy[(sr, sc, initial_mask)] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, steps = queue.popleft()

            if mask == full_mask:
                return steps

            if best_energy.get((r, c, mask), -1) > e:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = e - 1
                    if next_e < 0:
                        continue

                    next_mask = mask
                    cell_type = classroom[nr][nc]

                    if cell_type == 'L':
                        bit_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << bit_idx)

                    if cell_type == 'R':
                        next_e = energy

                    state_key = (nr, nc, next_mask)
                    if next_e > best_energy.get(state_key, -1):
                        best_energy[state_key] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))

        return -1