# Unit test reference

| Method | Checks that |
|-------|-------|
| assertEqual(a,b) | a==b  |
| assertNotEqual(a,b) | a != b |
| assertTrue(x) | bool(x) is True |
| assertFalse(x) | bool(x) is False |
| assertIs(a,b) | a is b |
| assertIs(a,b) | a is b |
| assertIsNot(a, b) | a is not b |
| assertIsNone(x) | x is None |
| assertIsNotNone(x) | x is not None |
| assertIn(a, b) | a in b |
| assertNotIn(a, b) | a not in b |
| assertIsInstance(a, b) | isinstance(a, b) |
| assertNotIsInstance(a, b) | not isinstance(a, b) |
[Table Source](https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example#__next)

```python
class Square(Shape):
    def __init__(self, length: float) -> None:
        if length < 0:
            raise ValueError('The length cannot be negative')
        self._length = length

class TestSquare(unittest.TestCase):

    def test_create_square_negative_length(self):
        with self.assertRaises(ValueError):
            square = Square(-1)
```
