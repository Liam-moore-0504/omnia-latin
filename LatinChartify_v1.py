import time
print("""
Welcome to Latin Chartify!
Seperate columns in a row with a comma
Row 0 is the row with your title
When you are done entering rows for your chart type 'make chart'
      """)

n = 1
print("Lets make the top row")
title = input("Title: ")
extra_info = input("Extra info. describing title: ")
v1 = input("Next value in this row: ")
v2 = input("Next value in this row: ")

if v1 == "":
      v1 = "Singular"
if v2 == "":
      v2 = "Plural"

rows = {}  # Dictionary to store rows with keys as n
html_rows = []

titlerow = (f"""
<table>
      <thead>
            <tr>
                  <th>{title} {extra_info}</th><td>{v1}</td><td>{v2}</td> 
            </tr>
      </thead> 
""")
persons = 0

while True:
      row = input(f"Row {n}: ")
      if "make" in row and "chart" in row:
            print(titlerow)
            for html_row in html_rows:
                  print(html_row.strip())
            print("</table>")
            time.sleep(120)
            break
      
      key = f"{n}row"
      rows[key] = row

      # Split the row into parts
      row_parts = rows[key].split(", ")
      if persons == 0:
            person = "1st Person"
      if persons == 1:
            person = "2nd Person"
      if persons == 2:
            person = "3rd Person"
      html_row = (f"""
      <tr>
            <td>{person}</td><td>{row_parts[0] if len(row_parts) > 0 else ''}</td><td>{row_parts[1] if len(row_parts) > 1 else ''}</td>
      </tr>
""")
      html_rows.append(html_row)
      n += 1
      persons +=1
