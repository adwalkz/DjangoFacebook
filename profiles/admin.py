from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin

from .models import Profile, Relationship


admin.site.register(Profile)
admin.site.register(Relationship)
