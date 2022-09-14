from src.counter import count_ocurrences


def test_counter():
    'a funcao count_ocurrences deve funcionar corretamente'
    count = count_ocurrences('src/jobs.csv', 'Python')
    assert count == 1639
    count = count_ocurrences('src/jobs.csv', 'Javascript')
    assert count != 10
