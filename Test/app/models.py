from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    # root_item = models.ManyToOneRel(MenuItem.title)

    def __str__(self):
        return "{0}".format(self.name)

    def save(self, *args, **kwargs):

        super(Menu, self).save(*args, **kwargs)

        current = 1000
        current2 = 100
        current3 = 10
        for item in MenuItem.objects.filter(menu=self, parent=None).order_by('order'):
            item.order = current
            item.save()
            current += 1000


        for item in MenuItem.objects.filter(menu=self, level=2).order_by('order'):
            item.order = current2 + item.parent.order
            item.save()
            current2 += 100

        for item in MenuItem.objects.filter(menu=self, level=3).order_by('order'):
            item.order = current3 + item.parent.order
            item.save()
            current3 += 10



class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    # level = models.PositiveIntegerField()
    menu = models.ForeignKey(Menu)
    order = models.IntegerField()
    parent = models.ForeignKey('self', blank=True, null=True)
    has_children = models.BooleanField(default=False)
    level = models.PositiveIntegerField()

    def save(self,*args,**kwargs):
        super(MenuItem, self).save(*args, **kwargs)

        if self.parent is not None:
            self.parent.has_children = True
            self.parent.save()



    def __str__(self):
        return "{0}".format(self.title)
