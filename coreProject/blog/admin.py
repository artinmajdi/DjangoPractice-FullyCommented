from django.contrib import admin
from .models import Post

""" You are telling the Django administration site that your model is registered in 
    the site using a custom class that inherits from ModelAdmin. In this class, you can 
    include information about how to display the model in the site and how to interact 
    with it """
    

""" The @admin.register(Post) decorator performs the same function as the admin.site.register(Post, PostAdmin),
    registering the ModelAdmin class that it decorates. 
    
        @admin.register(Post)   <- equivalent ->   admin.site.register(Post, PostAdmin)  """    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ columns of information showing in front of each post """
    list_display = ('title','slug','author','publish','status')
    
    """ list of filters that we can filter all posts on the right hand side of the page """
    list_filter = ('status','created','publish','author')
    
    """ items that it'll look into when user searches something inside the Post page """
    search_fields = ('title','body')
    
    """ when I click on New Post, by while entering something for the 'title', it will automaticcalt autofill 'slug' with that text """
    prepopulated_fields = {'slug': ('title',)}
    
    """ This will change the author field in creating New Post from their actual names to IDs """
    # raw_id_fields = ('author',)
    
    """ this will add a filter by date on top of the posts """
    date_hierarchy = 'publish'
    
    """ this says how to sort all of the blog posts in ascending order startin from 'author', then 'publish', then 'status' """
    ordering = ('author','publish','status')


""" Continue from 
        Working with QuerySets and managers     Django 3 By Example - Third Edition 
        https://learning.oreilly.com/library/view/django-3-by/9781838981952/Text/Chapter_1.xhtml
"""