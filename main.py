def pagination(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> str:
    if not all(
        isinstance(param, int)
        for param in [current_page, total_pages, boundaries, around]
    ):
        raise ValueError("All parameters must be integers")
    if total_pages < 1:
        raise ValueError("Invalid total_pages value")
    if not (1 <= current_page <= total_pages):
        raise ValueError("Invalid current_page value")
    if boundaries < 0:
        raise ValueError("Invalid boundaries value")
    if around < 0:
        raise ValueError("Invalid around value")

    if boundaries > total_pages:
        boundaries = total_pages

    ## O(n*log(n)) approach
    # result = set()

    # start = range(1, boundaries + 1)
    # around_current = range(
    #     max(1, current_page - around), min(total_pages, current_page + around) + 1
    # )
    # end = range(total_pages - boundaries + 1, total_pages + 1)

    #
    # result = sorted(result.union(start, around_current, end))

    ## O(n) approach
    result = []

    for i in range(1, boundaries + 1):
        result.append(i)

    start_around = max(1, current_page - around)
    end_around = min(total_pages, current_page + around)
    for i in range(start_around, end_around + 1):
        if i not in result:
            result.append(i)

    for i in range(total_pages - boundaries + 1, total_pages + 1):
        if i not in result:
            result.append(i)

    # result.sort()

    # beatify output
    pagination_str = ""
    previous_page = result[0] if result else None

    for page_num in result:
        if page_num - previous_page > 1:
            pagination_str += "... "
        pagination_str += f"{page_num} "
        previous_page = page_num

    if boundaries == 0 and result and result[0] > 1:
        pagination_str = "... " + pagination_str

    if boundaries == 0 and result and result[-1] < total_pages:
        pagination_str += "..."

    return pagination_str.strip()


if __name__ == "__main__":

    print(pagination(9, 10, 4, 1))
    print(pagination(10, 10, 3, 1))

    # import time
    # start = time.time()
    # pagination(500_000_000_000, 1_000_000_000_000, 1_000_000, 100_000)
    # end = time.time()
    # print(f"first {end-start}")
