import unittest

import app import ADD_TODO, DELETE_TODO, LIST_TODO, START_TODO, DUE_DATE, HELP_ME

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class BotTestCase(unittest.TestCase)
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "help me",
                KEY_EXPECTED: "Hello! I'm the agendasync textbot! My know commands are: 'add todo', 'delete todo, 'list todo', 'start date', and 'due date'"
            }
            # TODO add another
        ]
        
    def test_help_message(self):
        """successful help call"""
        for test in self.success_test_help:
            response = TESTOBJ.check_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)
    
if __name__ == "__main__":
    unittest.main()