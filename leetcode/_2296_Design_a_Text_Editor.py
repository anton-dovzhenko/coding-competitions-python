class TextEditor:

    class Node:
        def __init__(self, val, prev, nnext):
            self.val = val
            self.nnext = nnext
            self.prev = prev

        # def __repr__(self):
        #     return "%s->%s->%s" % (None if self.prev is None else self.prev.val,
        #                            self.val,
        #                            None if self.nnext is None else self.nnext.val)

    def __init__(self):
        self.cursor = TextEditor.Node(None, None, None)

    def addText(self, text: str) -> None:
        for c in text:
            nnext = self.cursor.nnext
            self.cursor.nnext = TextEditor.Node(c, self.cursor, nnext)
            self.cursor = self.cursor.nnext
            if nnext is not None:
                nnext.prev = self.cursor

    def deleteText(self, k: int) -> int:
        deleted_count = 0
        while k > 0 and self.cursor.val is not None:
            deleted = self.cursor
            self.cursor = self.cursor.prev
            self.cursor.nnext = deleted.nnext
            if deleted.nnext is not None:
                deleted.nnext.prev = self.cursor
            deleted.prev = None
            deleted.nnext = None
            deleted_count += 1
            k -= 1
        return deleted_count

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.cursor.val is not None:
            self.cursor = self.cursor.prev
            k -= 1
        return self.printLeft()

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.cursor is not None and self.cursor.nnext is not None:
            self.cursor = self.cursor.nnext
            k -= 1
        return self.printLeft()

    def printLeft(self, limit=10):
        result = ""
        cursor = self.cursor
        while limit > 0 and cursor.val is not None:
            result = cursor.val + result
            cursor = cursor.prev
            limit -= 1
        return result

