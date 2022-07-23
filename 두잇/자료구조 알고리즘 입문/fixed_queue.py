from typing import Any

class FixedQueue:

    class Empty(Exception):
        '''
        큐가 비어있을 때의 예외처리 class
        '''
        pass

    class Full(Exception):
        '''
        큐가 꽉차있을 때의 예외처리 class
        '''

    def __init__(self, capacity:int):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> bool:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x:Any) -> None:
        if self.is_full():
            raise  FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0                   # 맨 끝에 도달하면 0으로 만듬

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        '''
        피크 : 맨 앞 데이터를 들여다봄
        :return: 맨 앞 데이터
        '''
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value:Any) -> Any:
        '''
        큐에서 value를 찾아 인덱스를 반환 (없으면 -1 반환)
        :param value: 찾는 원소
        :return: 인덱스(없으면 -1)
        '''
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value:Any) -> int:
        '''
        큐에 있는 value의 개수를 반환
        :param value: 찾는 값
        :return: 개수
        '''
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, item) -> bool:
        return self.count(item) >= 1

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비어있음')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = '')
                print()