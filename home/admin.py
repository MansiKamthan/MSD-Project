from django.contrib import admin
from .models import PropertyType, PropertyNeighborhood, PropertyPricerange, Property, PropertyImage, Search

admin.site.register(PropertyType)
admin.site.register(PropertyNeighborhood)
admin.site.register(PropertyPricerange)
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Search)
