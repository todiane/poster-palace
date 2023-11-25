from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
 
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """use in templates to generate a link category page, 
        instead of hard-coding the URL"""
        return reverse('products:product_list_by_category',
                       args=[self.slug])


class Size(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)
    sizes = models.ManyToManyField(Size)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        
        index_together = (('id', 'slug'),) # add index_together
        ordering = ['name']

        verbose_name = 'product'
        verbose_name_plural = 'products'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       args=[self.id, self.slug])
