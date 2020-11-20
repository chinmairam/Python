from django.contrib import admin

# Register your models here.
from .models import Publisher, Author, Book

#admin.site.register(Publisher)
#admin.site.register(Author)
#admin.site.register(Book)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('authors',)
    ordering = ('title',)
    search_fields = ('authors',)