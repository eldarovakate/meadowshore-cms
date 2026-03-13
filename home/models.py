from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):

    hero_title = models.CharField(
        max_length=255,
        blank=True
    )

    hero_subtitle = models.CharField(
        max_length=255,
        blank=True
    )

    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    brand_text = RichTextField(
        blank=True
    )

    collection_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    collection_title = models.CharField(
        max_length=255,
        blank=True
    )

    collection_subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text="Маленький текст над заголовком, например: КОЛЛЕКЦИЯ · 2026"
    )

    collection_description = models.TextField(
        blank=True
    )

    content_panels = Page.content_panels + [

        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("hero_image"),
        FieldPanel("brand_text"),
        FieldPanel("collection_image"),
        FieldPanel("collection_title"),
        FieldPanel("collection_subtitle"),
        FieldPanel("collection_description"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["featured_products"] = (
            ProductPage.objects.child_of(self).live().filter(is_featured=True)
        )
        return context


class ProductPage(Page):

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = RichTextField(
        blank=True
    )

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    available_sizes = models.CharField(
        max_length=255,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    content_panels = Page.content_panels + [
        FieldPanel("price"),
        FieldPanel("description"),
        FieldPanel("main_image"),
        FieldPanel("available_sizes"),
        FieldPanel("is_featured"),
    ]

    parent_page_types = ["home.HomePage"]