class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        rows, cols = len(board), len(board[0])
        found: list[str] = []

        def dfs(r: int, c: int, parent: TrieNode) -> None:
            ch = board[r][c]
            curr = parent.children.get(ch)
            if curr is None:
                return

            if curr.word is not None:
                found.append(curr.word)
                curr.word = None

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, curr)
            board[r][c] = ch

            if not curr.children and curr.word is None:
                del parent.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return found