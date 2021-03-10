import html, re


def parse_table(source):
    table_headers = []
    table_contents = []
    table_break_flag = False

    lines = source.splitlines()

    for line in lines:
        #Add strings into table Contents
        #Remove whitespace on cells
        if line == '':
            continue

        if line[0] == '+' or line[0] ==  '|':
            line = line[1:]
        if line[-1] in ['+', '|']:
            line = line[:-1]

        raw_cells = re.split("\ \|\ |\-\+\-", line)

        cell_information = [x.strip() for x in raw_cells]
        #print(cell_information)

        #Add cel information into table contents
        table_contents.append(cell_information)

        #Check if cell contents are a table break
        if table_headers == []:
            for cell in cell_information:
                if bool(re.search("^-*$", cell)):
                    table_break_flag = True
                else:
                    table_break_flag = False
                    break

            if table_break_flag:
                table_headers = table_contents[0]
                table_contents = []
            
    return {"table_header":table_headers, "table_contents":table_contents}
    

def fence_table_format(source, language, class_name, options, md, **kwargs):
    """Format source as code blocks."""

    classes = kwargs['classes']
    id_value = kwargs['id_value']
    attrs = kwargs['attrs']

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ''
    classes = ' class="{}" data-sortable'.format(' '.join(classes)) if classes else ''
    attrs = ' ' + ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items()) if attrs else ''

    #Start Parsing table
    data = parse_table(source)

    #Generate HTML
    html_out = "<table{}{}{}><thead><tr>".format(id_value, classes, attrs)

    for header in data["table_header"]:
        html_out += "<th>{}</th>".format(html.escape(header))

    html_out += "</tr></thead><tbody>"

    for row in data["table_contents"]:
        html_out += "<tr>"
        for cell in row:
            html_out += "<td>{}</td>".format(html.escape(cell))
        html_out += "</tr>"

    html_out += "</tbody></table>"

    return html_out

def fence_tree_format(source, language, class_name, options, md, **kwargs):
    """Format source as code blocks."""

    classes = kwargs['classes']
    id_value = kwargs['id_value']
    attrs = kwargs['attrs']

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ''
    classes = ' class="{}"'.format(' '.join(classes)) if classes else ''
    attrs = ' ' + ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items()) if attrs else ''

    return '<pre%s%s%s><code>%s</code></pre>' % (id_value, classes, attrs, html.escape(source))

def fence_div_format(source, language, class_name, options, md, **kwargs):
    """Format source as div."""

    classes = kwargs['classes']
    id_value = kwargs['id_value']
    attrs = kwargs['attrs']

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ''
    classes = ' class="{}"'.format(' '.join(classes)) if classes else ''
    attrs = ' ' + ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items()) if attrs else ''

    return '<div%s%s%s>%s</div>' % (id_value, classes, attrs, html.escape(source))


if __name__ == "__main__":
    table1 = """|                | 32-bit syscall            | 64-bit syscall        |
+----------------+---------------------------+-----------------------+
| instruction    | int $0x80                 | syscall               |
| syscall number | EAX (execve = 0xb)        | RAX, (execve = 0x3b)  |
| 1-6 Args       | EBX|ECX|EDX|ESI|EDI|EBP   | RDI|RSI|RDX|R10|R8|R9 |
| 6+  Args       | EBX points to list in mem | Forbidden             |
"""
    print(parse_table(table1))