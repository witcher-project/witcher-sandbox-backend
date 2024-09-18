import django_filters


class PriceRangeFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        fields = ["price"]
