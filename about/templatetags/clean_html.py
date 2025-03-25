from django import template
import re

register = template.Library()


@register.filter
def clean_html_content(value):
    """
    Cleans the content by:
    - Removing <o:p> and </o:p> tags
    - Removing <style>...</style> tags
    - Removing Microsoft Office-specific CSS properties (e.g., mso-*)
    - Removing Unicode Private Use Area (PUA) characters (e.g., )
    - Removing unrecognized CSS at-rules (e.g., @list)
    """
    # Remove <o:p> and </o:p> tags
    value = re.sub(r'<\/?o:p>', '', value)

    # Remove <style> tags and their contents
    value = re.sub(r'<style.*?>.*?</style>', '', value, flags=re.DOTALL)

    # Remove Microsoft Office-specific CSS properties (e.g., mso-*)
    value = re.sub(r'mso-[a-z\-]+:[^;"]+;', '', value, flags=re.IGNORECASE)

    # Remove Unicode Private Use Area (PUA) characters (e.g., )
    value = re.sub(r'[\uE000-\uF8FF]', '', value)

    # Remove unrecognized CSS at-rules (e.g., @list)
    value = re.sub(r'@[\w\-]+.*?{.*?}', '', value, flags=re.DOTALL)

    return value
