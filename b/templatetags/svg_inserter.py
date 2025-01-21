import os
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def include_svg(file_name, **attrs):
    """
    Вставляет содержимое SVG-файла в HTML.

    :param file_name: Имя файла SVG (например, "icon.svg").
    :param attrs: Дополнительные атрибуты для тега SVG (например, class="my-class").
    :return: HTML-содержимое SVG или пустую строку, если файл не найден.
    """
    svg_dir = getattr(settings, "SVG_DIR", os.path.join(settings.BASE_DIR, "static", "svg"))
    svg_path = os.path.join(svg_dir, file_name)

    if not os.path.exists(svg_path):
        return f"<!-- SVG not found: {file_name} -->"

    try:
        with open(svg_path, "r", encoding="utf-8") as svg_file:
            svg_content = svg_file.read()

        # Добавляем атрибуты
        if attrs:
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(svg_content, "html.parser")
            svg_tag = soup.find("svg")
            if svg_tag:
                for key, value in attrs.items():
                    svg_tag[key] = value
                svg_content = str(soup)

        return mark_safe(svg_content)
    except Exception as e:
        return f"<!-- Error loading SVG: {e} -->"

# Пример настроек в settings.py
# SVG_DIR = os.path.join(BASE_DIR, "static", "svg")

# Пример использования в шаблоне:
# {% load svg_inserter %}
# {% include_svg "icon.svg" class="icon-class" id="icon-id" %}
