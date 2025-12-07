import os
from IPython.display import display, HTML
import glob

out_name = "gruyere_report"

def find_html_report(out):
    if os.path.isfile(out) and out.lower().endswith('.html'):
        return os.path.abspath(out)

    if os.path.isdir(out):
        matches = glob.glob(os.path.join(out, "*.html"))
        if matches:
            matches.sort(key=os.path.getmtime, reverse=True)
            return os.path.abspath(matches[0])

    candidates = glob.glob(out + "*/*.html") + glob.glob(out + "*.html")
    if candidates:
        candidates.sort(key=os.path.getmtime, reverse=True)
        return os.path.abspath(candidates[0])

    return None

report_path = find_html_report(out_name)
if report_path:
    print("Report file found:", report_path)
    with open(report_path, 'r', encoding='utf-8') as f:
        html = f.read()
    display(HTML(html))
else:
    print("No HTML report found.")
