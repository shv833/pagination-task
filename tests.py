import unittest
from main import pagination


class TestPagination(unittest.TestCase):
    def test_valid_pagination(self):
        scenarios = [
            {
                "current_page": 2,
                "total_pages": 10,
                "boundaries": 3,
                "around": 1,
                "expected": "1 2 3 ... 8 9 10",
            },
            {
                "current_page": 6,
                "total_pages": 10,
                "boundaries": 1,
                "around": 3,
                "expected": "1 ... 3 4 5 6 7 8 9 10",
            },
            {
                "current_page": 6,
                "total_pages": 10,
                "boundaries": 0,
                "around": 3,
                "expected": "... 3 4 5 6 7 8 9 ...",
            },
            {
                "current_page": 4,
                "total_pages": 5,
                "boundaries": 1,
                "around": 0,
                "expected": "1 ... 4 5",
            },
            {
                "current_page": 4,
                "total_pages": 5,
                "boundaries": 0,
                "around": 0,
                "expected": "... 4 ...",
            },
            {
                "current_page": 50,
                "total_pages": 100,
                "boundaries": 0,
                "around": 2,
                "expected": "... 48 49 50 51 52 ...",
            },
            {
                "current_page": 4,
                "total_pages": 10,
                "boundaries": 2,
                "around": 2,
                "expected": "1 2 3 4 5 6 ... 9 10",
            },
            {
                "current_page": 10,
                "total_pages": 1_000_000_000_000_000_000_000,
                "boundaries": 5,
                "around": 3,
                "expected": "1 2 3 4 5 ... 7 8 9 10 11 12 13 ... 999999999999999999996 999999999999999999997 999999999999999999998 999999999999999999999 1000000000000000000000",
            },
            {
                "current_page": 1,
                "total_pages": 1,
                "boundaries": 0,
                "around": 0,
                "expected": "1",
            },
            {
                "current_page": 1,
                "total_pages": 1,
                "boundaries": 1,
                "around": 1,
                "expected": "1",
            },
            {
                "current_page": 5,
                "total_pages": 5,
                "boundaries": 1,
                "around": 0,
                "expected": "1 ... 5",
            },
            {
                "current_page": 2,
                "total_pages": 10,
                "boundaries": 0,
                "around": 4,
                "expected": "1 2 3 4 5 6 ...",
            },
            {
                "current_page": 2,
                "total_pages": 10,
                "boundaries": 0,
                "around": 40,
                "expected": "1 2 3 4 5 6 7 8 9 10",
            },
            {
                "current_page": 2,
                "total_pages": 10,
                "boundaries": 100,
                "around": 0,
                "expected": "1 2 3 4 5 6 7 8 9 10",
            },
        ]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                self.assertEqual(
                    pagination(
                        scenario["current_page"],
                        scenario["total_pages"],
                        scenario["boundaries"],
                        scenario["around"],
                    ),
                    scenario["expected"],
                )

    def test_invalid_current_page(self):
        scenarios = [
            {
                "current_page": 0,
                "total_pages": 5,
                "boundaries": 1,
                "around": 0,
            },
            {
                "current_page": 6,
                "total_pages": 5,
                "boundaries": 1,
                "around": 0,
            },
        ]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                with self.assertRaises(ValueError):
                    pagination(
                        scenario["current_page"],
                        scenario["total_pages"],
                        scenario["boundaries"],
                        scenario["around"],
                    )

    def test_invalid_total_pages(self):
        scenarios = [
            {
                "current_page": 4,
                "total_pages": 0,
                "boundaries": 1,
                "around": 0,
            }
        ]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                with self.assertRaises(ValueError):
                    pagination(
                        scenario["current_page"],
                        scenario["total_pages"],
                        scenario["boundaries"],
                        scenario["around"],
                    )

    def test_invalid_boundaries(self):
        scenarios = [
            {
                "current_page": 4,
                "total_pages": 5,
                "boundaries": -1,
                "around": 0,
            }
        ]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                with self.assertRaises(ValueError):
                    pagination(
                        scenario["current_page"],
                        scenario["total_pages"],
                        scenario["boundaries"],
                        scenario["around"],
                    )

    def test_invalid_around(self):
        scenarios = [
            {
                "current_page": 4,
                "total_pages": 5,
                "boundaries": 1,
                "around": -1,
            }
        ]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                with self.assertRaises(ValueError):
                    pagination(
                        scenario["current_page"],
                        scenario["total_pages"],
                        scenario["boundaries"],
                        scenario["around"],
                    )

    def test_non_integer_input(self):
        scenarios = [
            {
                "current_page": "abc",
                "total_pages": 5,
                "boundaries": 1,
                "around": 0,
            },
            {
                "current_page": 4,
                "total_pages": 5,
                "boundaries": "def",
                "around": 0,
            },
            {
                "current_page": 4.1,
                "total_pages": [12, 4],
                "boundaries": "def",
                "around": 1242.3,
            },
            {
                "current_page": 4,
                "total_pages": 5,
                "boundaries": 1,
                "around": "ghi",
            },
            {
                "current_page": "jkl",
                "total_pages": "mno",
                "boundaries": "pqr",
                "around": "stu",
            },
        ]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                with self.assertRaises(ValueError):
                    pagination(
                        scenario["current_page"],
                        scenario["total_pages"],
                        scenario["boundaries"],
                        scenario["around"],
                    )


if __name__ == "__main__":
    unittest.main()
