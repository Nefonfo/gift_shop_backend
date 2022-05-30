from django.utils.html import format_html
from wagtail.images.formats import Format, register_image_format


class TailwindImageFormat(Format):
    def image_to_html(self, image, alt_text, extra_attributes=None):
        default_html = super().image_to_html(image, alt_text, extra_attributes)

        return format_html(
            "<div class='w-full flex justify-center'>{}</div>", default_html
        )


register_image_format(
    TailwindImageFormat(
        "tailwind_formated", "Theme Tailwind Format", "w-full md:w-1/2 my-10", "original"
    )
)