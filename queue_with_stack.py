class Queue:
    def __init__(self) -> None:
        # enqueue 할 때 쓸 스택
        self.enqueue_stack = []
        # dequeue 할 때 쓸 스택
        self.dequeue_stack = []
        
    def enqueue(self, data):
        # queue에 아이템 넣기 O(1)
        self.enqueue_stack.append(data)
        
    def dequeue(self):
        # 두 stack 모두 아이템이 하나도 없을 경우 raise Exception 하기
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty")
        # dequeue_stack 이 비어있으면 enqueue_stack에서 pop해서 넣기 O(n)
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
    

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    
    print(f' queue.dequeue : {queue.dequeue()}')
    print(f' queue.dequeue : {queue.dequeue()}')
    print(f' queue.dequeue : {queue.dequeue()}')
    print(f' queue.dequeue : {queue.dequeue()}')
