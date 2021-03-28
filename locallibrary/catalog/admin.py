from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)


# Register the Admin classes for Author using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth',
                    'date_of_death')
    # 字段默认情况下垂直显示，但如果进一步将它们分组在元组中（如上述“日期”字段中所示），则会水平显示。
    # 注意：还可以使用exclude属性来声明要从表单中排除的属性列表（将显示模型中的所有其他属性）。
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 我们不能直接指定 list_display 中的 genre 字段， 因为它是一个ManyToManyField
    # （Django可以防止这种情况，因为在这样做时会有大量的数据库访问“成本”）。
    # 相反，我们将在 Book 模型中定义一个 display_genre 函数来获取信息作为一个字符串
    list_display = ('title', 'author', 'display_genre')


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')


# Register the Admin classes for Genre using the decorator
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
