import os
import tempfile
from unittest import TestCase
from unittest.mock import MagicMock
from aider.commands import Commands
from aider.io import InputOutput

class TestCommands(TestCase):
    def test_cmd_add(self):
        # Create a temporary directory and change the current working directory
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chdir(tmpdir)

            # Initialize the Commands and InputOutput objects
            io = InputOutput(pretty=False, yes=True)
            coder = MagicMock()
            commands = Commands(io, coder)

            # Call the cmd_add method with 'foo.txt' and 'bar.txt'
            commands.cmd_add(["foo.txt", "bar.txt"])

            # Check if both files have been created in the temporary directory
            self.assertTrue(os.path.exists("foo.txt"))
            self.assertTrue(os.path.exists("bar.txt"))
