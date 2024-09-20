from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Desc"

    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )

    def test_create_amenity(self):

        new_amenity_name = "New Amenity"
        new_amenity_desc = "New amenity desc."

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_desc,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_desc,
        )

        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)


class TestAmenity(APITestCase):

    NAME = "Test Amenity"
    DESC = "Test DESC"
    URL = "/api/v1/rooms/amenities/1"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):

        upd_amenity_name = "Update Name"
        upd_amenity_desc = "Update DESC"

        # (Nothing update)
        response = self.client.put(self.URL)
        self.assertEqual(response.status_code, 200)

        # (Update)
        response = self.client.put(
            self.URL,
            data={
                "name": upd_amenity_name,
                "description": upd_amenity_desc,
            },
        )
        data = response.json()

        # Valid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data["name"],
            upd_amenity_name,
        )
        self.assertEqual(
            data["description"],
            upd_amenity_desc,
        )

        # Invalid - max_length=150
        self.assertLessEqual(len(data["name"]), 150)
        # invalid_name = "test" * 40
        # response = self.client.put(
        #     self.URL,
        #     data={"name": invalid_name},
        # )
        # self.assertEqual(response.status_code, 400)

    def test_delete_amenity(self):

        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 204)
