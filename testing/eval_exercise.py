from unittest import TestCase


class Evaluate(TestCase):
    def test_hello_world(self):
        import exercise
        self.assertEqual(exercise.hello_world(), "Hello World")


