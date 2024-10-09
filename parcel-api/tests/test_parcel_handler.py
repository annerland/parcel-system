import unittest
from fastapi.testclient import TestClient
from api import app
import os

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.test_xml_file = 'Container_68465468.xml'
        self.create_test_xml()

    def create_test_xml(self):
        xml_content = """
        <Container>
            <parcels>
                <Parcel>
                    <Receipient>
                        <Name>Test User</Name>
                    </Receipient>
                    <Weight>0.5</Weight>
                    <Value>100</Value>
                </Parcel>
                <Parcel>
                    <Receipient>
                        <Name>Test User 2</Name>
                    </Receipient>
                    <Weight>5.0</Weight>
                    <Value>1500</Value>
                </Parcel>
            </parcels>
        </Container>
        """
        with open(self.test_xml_file, 'w') as f:
            f.write(xml_content)

    def tearDown(self):
        os.remove(self.test_xml_file)

    def test_get_parcels(self):
        response = self.client.get("/parcels")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data["parcels"]), 2)
        
        self.assertEqual(data["parcels"][0]["name"], "Test User")
        self.assertEqual(data["parcels"][0]["weight"], 0.5)
        self.assertEqual(data["parcels"][0]["value"], 100)
        self.assertEqual(data["parcels"][0]["department"], "MailDepartment")

        self.assertEqual(data["parcels"][1]["name"], "Test User 2")
        self.assertEqual(data["parcels"][1]["weight"], 5.0)
        self.assertEqual(data["parcels"][1]["value"], 1500)
        self.assertEqual(data["parcels"][1]["department"], "InsuranceDepartment")

if __name__ == '__main__':
    unittest.main()