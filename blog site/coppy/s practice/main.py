# Generate HTML content using Python
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python-Generated HTML</title>
</head>
<body>
    <h1>Hello from Python!</h1>
    <p>This HTML content was generated using Python.</p>
</body>
</html>
"""

# Write the HTML content to a file
with open('generated_html.html', 'w') as f:
    f.write(html_content)

