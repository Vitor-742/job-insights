from src.counter import count_ocurrences


def test_counter():
    'a funcao count_ocurrences deve funcionar corretamente'
    count = count_ocurrences('src/jobs.csv', 'Python')
    print(type(count))
    assert count is 1639