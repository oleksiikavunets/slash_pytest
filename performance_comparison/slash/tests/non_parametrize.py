import slash


@slash.tag('slash_non_parametrize')
@slash.repeat(1000)
def test_non_parametrize_1():
    assert 1 == 1


@slash.tag('slash_non_parametrize')
@slash.repeat(1000)
def test_non_parametrize_2():
    assert 2 == 3
