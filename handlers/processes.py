def format_processes(processes, level=0):
    if not processes:
        return ''

    table = '<table class="process-table">'

    # Add table header
    table += '<thead><tr><th>PID</th>'
    for key in processes[0].keys():
        if key != 'children':
            table += f'<th>{key}</th>'
    table += '</tr></thead>'

    # Add table body
    table += '<tbody>'
    for process in processes:
        table += f'<tr data-level="{level}"><td>{process["pid"]}</td>'
        for key, value in process.items():
            if key != 'children':
                table += f'<td>{value}</td>'
        table += '</tr>'
        if 'children' in process:
            table += f'<tr class="child-row" data-level="{level + 1}"><td></td><td colspan="{len(process) - 1}">{format_processes(process["children"], level + 1)}</td></tr>'
    table += '</tbody></table>'

    return table

def process_tree_html(processes, level=0):
    html = ""
    for process in processes:
        # add row for current process
        html += "<tr style='background-color: {};'>".format(get_color(level))
        html += "<td>{}</td>".format(process["pid"])
        for key in process.keys():
            if key != "children":
                html += "<td>{}</td>".format(process[key])
        html += "</tr>"
        # add rows for children
        if "children" in process.keys():
            children_html = process_tree_html(process["children"], level + 1)
            html += "<tr><td></td><td colspan='{}'>{}</td></tr>".format(len(process.keys()) - 1,
                                                                         "<table>" + children_html + "</table>")
    return html

def get_color(level):
    colors = ["#ffc2b3", "#ffffcc", "#b3d9ff", "#b3ffb3", "#ffb3d9"]
    return colors[level % len(colors)]