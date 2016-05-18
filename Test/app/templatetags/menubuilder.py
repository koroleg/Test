from django import template
from django.template import loader

from app.models import MenuItem, Menu

register = template.Library()
# @register.inclusion_tag('purpose.html')
def build_menu(parser, token):
    """
    {% draw menu_name %}
    """
    try:
        tag_name, menu_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError("%r tag requires exactly one argument" % token.contents.split()[0])
    return MenuObject(menu_name)


class MenuObject(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        current_path = context['request'].path
        context['menuitems'] = get_items(self.menu_name, current_path)
        return ''

def get_items(menu_name, current_path):

    try:
        menu = Menu.objects.get(slug=menu_name)
    except Menu.DoesNotExist:
        return []
    menuitems = []
    lst = MenuItem.objects.filter(menu=menu).order_by('order')

    levels = []
    for i in lst:
        levels.append(i.level)
    levels.append(0)


    for index, i in enumerate(MenuItem.objects.filter(menu=menu).order_by('order')):

        current = (i.url != '/' and current_path == i.url)
        prevlevel = levels[index+1]
        menuitems.append({'url': i.url, 'title': i.title, 'current': current, 'order': i.order, 'has_children': i.has_children, 'level' : i.level, 'prevlevel': prevlevel})
    return menuitems

register.tag('draw', build_menu)