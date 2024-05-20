import unittest
import time


def pagination(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    if not all(isinstance(param, int) for param in [current_page, total_pages, boundaries, around]):
        return "All parameters must be integers"
    if total_pages < 1:
        return "Invalid total_pages value"
    if not (1 <= current_page <= total_pages):
        return "Invalid current_page value"
    if boundaries < 0 or boundaries > total_pages:
        return "Invalid boundaries value"
    if around < 0 or around >= current_page or current_page + around > total_pages:
        return "Invalid around value"

    result = set()

    start = range(1, boundaries + 1)
    around_current = range(max(1, current_page - around), min(total_pages, current_page + around) + 1)
    end = range(total_pages - boundaries + 1, total_pages + 1)

    result = sorted(result.union(start, around_current, end))

    # beatify output
    pagination_str = ""
    prev_page = result[0] if result else None

    for page_num in result:
        if page_num - prev_page > 1:
            pagination_str += "... "
        pagination_str += f"{page_num} "
        prev_page = page_num

    if boundaries == 0 and result and result[0] > 1:
        pagination_str = "... " + pagination_str

    if boundaries == 0 and result and result[-1] < total_pages:
        pagination_str += "..."

    return pagination_str.strip()


class TestPagination(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.invalid_around_msg = "Invalid around value"
        cls.invalid_boundaries_msg = "Invalid boundaries value"
        cls.invalid_current_page_msg = "Invalid current_page value"
        cls.invalid_total_pages_msg = "Invalid total_pages value"
        cls.invalid_instance_msg = "All parameters must be integers"

    def test_valid_pagination(self):
        self.assertEqual(pagination(2, 10, 3, 1), "1 2 3 ... 8 9 10")
        self.assertEqual(pagination(6, 10, 1, 3), "1 ... 3 4 5 6 7 8 9 10")
        self.assertEqual(pagination(6, 10, 0, 3), "... 3 4 5 6 7 8 9 ...")
        self.assertEqual(pagination(4, 5, 1, 0), "1 ... 4 5")
        self.assertEqual(pagination(4, 5, 0, 0), "... 4 ...")
        self.assertEqual(pagination(50, 100, 0, 2), "... 48 49 50 51 52 ...")
        self.assertEqual(pagination(4, 10, 2, 2), "1 2 3 4 5 6 ... 9 10")
        self.assertEqual(
            pagination(10, 1_000_000_000_000_000_000_000, 5, 3),
            "1 2 3 4 5 ... 7 8 9 10 11 12 13 ... 999999999999999999996 999999999999999999997 999999999999999999998 999999999999999999999 1000000000000000000000",
        )

    def test_invalid_current_page(self):
        self.assertEqual(pagination(0, 5, 1, 0), self.invalid_current_page_msg)
        self.assertEqual(pagination(6, 5, 1, 0), self.invalid_current_page_msg)

    def test_invalid_total_pages(self):
        self.assertEqual(pagination(4, 0, 1, 0), self.invalid_total_pages_msg)

    def test_invalid_boundaries(self):
        self.assertEqual(pagination(4, 5, -1, 0), self.invalid_boundaries_msg)
        self.assertEqual(pagination(4, 5, 6, 0), self.invalid_boundaries_msg)

    def test_invalid_around(self):
        self.assertEqual(pagination(4, 5, 1, -1), self.invalid_around_msg)
        self.assertEqual(pagination(14, 100, 10, 30), self.invalid_around_msg)
        self.assertEqual(pagination(61, 100, 10, 40), self.invalid_around_msg)
        self.assertEqual(pagination(10, 10, 0, 1), self.invalid_around_msg)

    def test_non_integer_input(self):
        self.assertEqual(pagination("abc", 5, 1, 0), self.invalid_instance_msg)
        self.assertEqual(pagination(4, 5, "def", 0), self.invalid_instance_msg)
        self.assertEqual(pagination(4.1, [12, 4], "def", 1242.3), self.invalid_instance_msg)
        self.assertEqual(pagination(4, 5, 1, "ghi"), self.invalid_instance_msg)
        self.assertEqual(pagination("jkl", "mno", "pqr", "stu"), self.invalid_instance_msg)


if __name__ == "__main__":
    a = input("Do you want to run unittests or manual test? (choices: unit/manual)")
    if a == "unit":
        unittest.main()
    else:
        print(pagination(200, 1_000_000_000_000, 10, 100))
        print(pagination(1234, 500000, 10, 30))
        print(pagination(50, 100, 0, 2))
        print(pagination(4, 10, 2, 2))

        # start = time.time()
        # with open('huge_test.txt', 'w') as file:
        #     print(pagination(500_000_000_000, 1_000_000_000_000, 1_000_000, 1_000), file=file)
        # end = time.time()
        # print(end-start)
