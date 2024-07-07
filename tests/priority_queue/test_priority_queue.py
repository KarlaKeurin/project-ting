from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 6})
    queue.enqueue({"qtd_linhas": 1})

    assert len(queue) == 3

    assert queue.search(0) == {"qtd_linhas": 4}
    assert queue.search(1) == {"qtd_linhas": 1}
    assert queue.search(2) == {"qtd_linhas": 6}

    assert queue.dequeue() == {"qtd_linhas": 4}
    assert queue.dequeue() == {"qtd_linhas": 1}
    assert queue.dequeue() == {"qtd_linhas": 6}

    with pytest.raises(IndexError):
        queue.search(10)
