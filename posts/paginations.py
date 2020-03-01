from rest_framework.pagination import PageNumberPagination


PAGE_SIZE = 2


class PostsPagination(PageNumberPagination):
    page_size = PAGE_SIZE
