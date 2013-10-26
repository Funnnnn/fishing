from .models import Lake, Type, Rank, Item, Exchange, Component
from django.contrib import admin

for model in (Lake, Type, Rank, Item, Exchange, Component):
    admin.site.register(model)
