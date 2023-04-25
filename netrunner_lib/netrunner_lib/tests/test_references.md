# Unit test reference

| Method | Checks that |
|-------|-------|
| assertEqual(a,b,msg) | a==b  |
| assertNotEqual(a,b,msg) | a != b |
| assertTrue(x,msg) | bool(x) is True |
| assertFalse(x,msg) | bool(x) is False |
| assertIs(a,b,msg) | a is b |
| assertIs(a,b,msg) | a is b |
| assertIsNot(a, b,msg) | a is not b |
| assertIsNone(x,msg) | x is None |
| assertIsNotNone(x,msg) | x is not None |
| assertIn(a, b,msg) | a in b |
| assertNotIn(a, b,msg) | a not in b |
| assertIsInstance(a, b,msg) | isinstance(a, b) |
| assertNotIsInstance(a, b,msg) | not isinstance(a, b) |
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
