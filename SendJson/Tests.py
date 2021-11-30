import TestCase01
import TestCase02
import unittest
from unittest import IsolatedAsyncioTestCase
class Tests(IsolatedAsyncioTestCase):
   ## async def test_response(self):
     #### self.assertEqual(response.status_code, 200, 'contract not created')
    async def test_result(self):
        response = TestCase02.emptyUMR()
        self.assertEqual(response.status_code, 200, 'successfull')
if __name__ == "__main__":
     unittest.main()
