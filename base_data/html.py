


def create_html_table(queryset):
    # Extract headers dynamically from the model's fields
    try:
        headers = [field.verbose_name for field in queryset.model._meta.fields]
    except :
        return "No Header"

    rows = list(queryset.values_list())

    html = f"<table class='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 border-spacing-x-11'>\n"

    # Add table headers
    html += "<tr class='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'>"
    for header in headers:
        html += "<th>{}</th>".format(header.capitalize())  # You might want to capitalize the headers
    html += "</tr>\n"

    # Add table rows
    for row in rows:
        html += "<tr>"
        for item in row:
            html += "<td>{}</td>".format(item)
        html += "</tr>\n"

    html += "</table>"

    return html