import pytest

import sqlparse


@pytest.mark.parametrize('mode', ['strip_whitespace', 'reindent'])
def test_keyword_transform_preserves_multiple_literals(mode):
    left = "'select a\\\nb  \r\nc'"
    right = "'from d\\\ne  \r\nf'"
    text = f'select {left} as x,\n{right} as y;'

    actual = sqlparse.format(text, keyword_case='upper', **{mode: True})

    assert actual.startswith('SELECT ')
    assert actual.count(' AS ') == 2
    assert left in actual
    assert right in actual
