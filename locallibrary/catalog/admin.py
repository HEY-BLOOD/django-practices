from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language
"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)


# 内联类，TabularInline (水平布局 ) or StackedInline (垂直布局 ，就像默认布局)
class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance
    # 只显示“Add another Book instance”链接，而不显示备用的实例编辑表单
    extra = 0


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book
    extra = 0


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('last_name', 'first_name', 'date_of_birth',
                    'date_of_death')
    # 字段默认情况下垂直显示，但如果进一步将它们分组在元组中（如上述“日期”字段中所示），则会水平显示。
    # 注意：还可以使用exclude属性来声明要从表单中排除的属性列表（将显示模型中的所有其他属性）。
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
