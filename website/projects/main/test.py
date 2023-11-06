import unittest
import subprocess
import sys

class TestMain(unittest.TestCase):

    def test_returncode(self):
        completedProc = subprocess.run("./build/binary/main.exe")
        self.assertEqual(0, completedProc.returncode)

if __name__ == '__main__':
    unittest.main()
