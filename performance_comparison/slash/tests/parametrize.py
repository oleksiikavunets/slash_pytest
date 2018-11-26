import slash


@slash.tag('slash_parametrize')
@slash.parametrize(('x', 'y'), [(1, 1), (2, 3)])
@slash.repeat(1000)
def test_parametrize(x, y):
    assert x == y
