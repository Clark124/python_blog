from django.core.paginator import Paginator


def paginator_dic(query_set, page_size, page_num):
    paginator = Paginator(query_set, page_size)
    # paginator
    page = paginator.page(page_num)
    count = paginator.count
    page_range = paginator.page_range
    pages_number = paginator.num_pages
    per_page = paginator.per_page
    # page
    has_next = page.has_next()
    has_previous = page.has_previous()
    current_page = page.number
    current_num = len(page)
    try:
        next_number = page.next_page_number()
    except:
        next_number = None

    try:
        pre_number = page.previous_page_number()
    except:
        pre_number = None

    return {
        "list": page,
        "count": count,
        "page_range": page_range,
        "number_pages": pages_number,
        "per_page": per_page,
        "has_next": has_next,
        "next_number": next_number,
        "pre_number": pre_number,
        "has_previous": has_previous,
        "current_page": current_page,
        "current_num": current_num

    }
