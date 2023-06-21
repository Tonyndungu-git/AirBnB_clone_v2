import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestDoCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_create_with_valid_parameters(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create BaseModel name="Test Object" value=10.5 count=3')
            output = mock_stdout.getvalue().strip()

            # Verify output
            self.assertRegex(output, r'^\[BaseModel\] \(.+\)$')

            # Verify object creation and parameters
            created_object = list(storage.all().values())[0]
            self.assertEqual(created_object.__class__.__name__, 'BaseModel')
            self.assertEqual(created_object.name, 'Test Object')
            self.assertEqual(created_object.value, 10.5)
            self.assertEqual(created_object.count, 3)

    def test_create_with_invalid_parameter_format(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create BaseModel invalid_param')
            output = mock_stdout.getvalue().strip()

            # Verify output
            self.assertEqual(output, 'Invalid parameter format')

            # Verify no object creation
            self.assertEqual(len(storage.all()), 0)

    def test_create_with_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create')
            output = mock_stdout.getvalue().strip()

            # Verify output
            self.assertEqual(output, '** class name missing **')

            # Verify no object creation
            self.assertEqual(len(storage.all()), 0)

    def test_create_with_nonexistent_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create NonExistentClass')
            output = mock_stdout.getvalue().strip()

            # Verify output
            self.assertEqual(output, '** class doesn\'t exist **')

            # Verify no object creation
            self.assertEqual(len(storage.all()), 0)


if __name__ == '__main__':
    unittest.main()
