from django.contrib import admin
from .models import Home, About, Portfolio, Role,Contact
from django.utils.html import format_html

class HomeAdmin(admin.ModelAdmin):
    list_display = ("name", "image_preview", "url1", "url2", "url3", "url4")
    list_filter = ("role",) 
    search_fields = ("name", "role__name")  
    readonly_fields = ("image_preview",)  
    list_per_page = 10 

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 5px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Preview" 

    filter_horizontal = ("role",)

admin.site.register(Home, HomeAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ("position", "mail", "phone", "age")
    search_fields = ("position", "mail")

admin.site.register(About, AboutAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "technologies", "github_link")
    search_fields = ("title", "technologies")

admin.site.register(Portfolio, PortfolioAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Role, RoleAdmin)
admin.site.register(Contact)

