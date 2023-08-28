class DoubleNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = DoubleNode(homepage)

    def visit(self, url: str) -> None:
        # that means url is now the new tail
        self.cur.next = DoubleNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        # if the number of steps becomes bigger than x, go back the most you can, so that there's a limit
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev  # the current page is now the previous page of the current page
            steps -= 1  # diminish 1 step
        return self.cur.val  # once the steps end, return the page you're at

    def forward(self, steps: int) -> str:  # same thing, but forward this time
        while self.cur.next and steps > 0:
            self.cur = self.cur.next  # instead of self.cur.prev it's self.cur.next
            steps -= 1
        return self.cur.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)