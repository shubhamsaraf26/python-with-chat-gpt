import os
from django.core.management import call_command

# Step 1: Create a new Django project
project_name = "mywebsite"
call_command("startproject", project_name)

# Step 2: Navigate into the project directory
os.chdir(project_name)

# Step 3: Create a new Django app
app_name = "myapp"
call_command("startapp", app_name)

# Step 4: Create the base.html template
base_template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Website{% endblock %}</title>
    <style>
        /* Add your CSS styles here */
        nav {
            background-color: #f2f2f2;
            padding: 10px;
            margin-bottom: 20px;
        }
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{% url 'home' %}">Home</a></li>
            <li><a href="{% url 'sanity' %}">Sanity</a></li>
            <li><a href="{% url 'health_check' %}">Health Check</a></li>
            <li><a href="{% url 'backup_check' %}">Backup Check</a></li>
        </ul>
    </nav>
    <hr>
    {% block content %}
    {% endblock %}
</body>
</html>
"""
templates_dir = os.path.join(app_name, "templates")
os.makedirs(templates_dir)
with open(os.path.join(templates_dir, "base.html"), "w") as base_template_file:
    base_template_file.write(base_template_content)

# Step 5: Create individual HTML templates for each tab
for tab in ["home", "sanity", "health_check", "backup_check"]:
    template_content = f"""{{% extends 'base.html' %}}

{{% block title %}}{tab.capitalize()} - My Website{{% endblock %}}

{{% block content %}}
<h1>{tab.capitalize()} Page</h1>
<!-- Add content specific to the {tab} page here -->
{{% endblock %}}
"""
    with open(os.path.join(templates_dir, f"{tab}.html"), "w") as template_file:
        template_file.write(template_content)

# Step 6: Define views for each tab
views_content = f"""from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sanity(request):
    return render(request, 'sanity.html')

def health_check(request):
    return render(request, 'health_check.html')

def backup_check(request):
    return render(request, 'backup_check.html')
"""
with open(os.path.join(app_name, "views.py"), "w") as views_file:
    views_file.write(views_content)

# Step 7: Define URL patterns for each view
urls_content = f"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sanity/', views.sanity, name='sanity'),
    path('health_check/', views.health_check, name='health_check'),
    path('backup_check/', views.backup_check, name='backup_check'),
]
"""
with open(os.path.join(app_name, "urls.py"), "w") as urls_file:
    urls_file.write(urls_content)

# Step 8: Update the project's urls.py file to include the URL patterns of the app
project_urls_content = f"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{app_name}.urls')),
]
"""
with open(os.path.join(project_name, "urls.py"), "w") as project_urls_file:
    project_urls_file.write(project_urls_content)

print("Website created successfully!")
