import unittest
from aprova_crew.src.aprova_crew.agent import Agent


class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent(name="TestAgent")

    def test_agent_initialization(self):
        self.assertEqual(self.agent.name, "TestAgent")

    def test_agent_perform_task(self):
        result = self.agent.perform_task("Sample Task")
        self.assertTrue(result)
        self.assertEqual(result, "Task Sample Task performed successfully!")


if __name__ == "__main__":
    unittest.main()
