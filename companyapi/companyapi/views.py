from django.http import HttpResponse,JsonResponse


def general_page(request):
    dictionary={
        'name':'Manav',
        'age':21,
        'college':'Dharmsinh Desai University',
        'semester':8
    }
    return JsonResponse(dictionary)

def home_page(request):
    htmlContent = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
                color: white;
                padding: 10px 0;
                text-align: center;
            }
            nav {
                background-color: #444;
                display: flex;
                justify-content: center;
                padding: 10px;
            }
            nav a {
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                margin: 0 10px;
            }
            nav a:hover {
                background-color: #575757;
            }
            .content {
                padding: 20px;
                text-align: center;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <!-- Header -->
        <header>
            <h1>Welcome to the Home Page</h1>
        </header>
        
        <!-- Navigation Bar -->
        <nav>
            <a href="/home">Home</a>
            <a href="/about">About</a>
            <a href="/services">Services</a>
            <a href="/contact">Contact</a>
        </nav>
        
        <!-- Main Content -->
        <div class="content">
            <h2>Explore Our Website</h2>
            <p>Discover the best content and services right here on our homepage. Stay connected for updates!</p>
        </div>
        
        <!-- Footer -->
        <footer>
            <p>&copy; 2024 My Website. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(htmlContent)

def about_page(request):
    htmlContent = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
                color: white;
                padding: 10px 0;
                text-align: center;
            }
            nav {
                background-color: #444;
                display: flex;
                justify-content: center;
                padding: 10px;
            }
            nav a {
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                margin: 0 10px;
            }
            nav a:hover {
                background-color: #575757;
            }
            .content {
                padding: 20px;
                text-align: center;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>About Us</h1>
        </header>
        <nav>
            <a href="/home">Home</a>
            <a href="/about">About</a>
            <a href="/services">Services</a>
            <a href="/contact">Contact</a>
        </nav>
        <div class="content">
            <h2>Who We Are</h2>
            <p>Learn about our mission, vision, and the amazing team behind our success.</p>
        </div>
        <footer>
            <p>&copy; 2024 My Website. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(htmlContent)

def services_page(request):
    htmlContent = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Services Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
                color: white;
                padding: 10px 0;
                text-align: center;
            }
            nav {
                background-color: #444;
                display: flex;
                justify-content: center;
                padding: 10px;
            }
            nav a {
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                margin: 0 10px;
            }
            nav a:hover {
                background-color: #575757;
            }
            .content {
                padding: 20px;
                text-align: center;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Our Services</h1>
        </header>
        <nav>
            <a href="/home">Home</a>
            <a href="/about">About</a>
            <a href="/services">Services</a>
            <a href="/contact">Contact</a>
        </nav>
        <div class="content">
            <h2>What We Offer</h2>
            <p>Explore the range of services we provide to meet your needs. From consulting to development, we do it all.</p>
        </div>
        <footer>
            <p>&copy; 2024 My Website. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(htmlContent)

def contact_page(request):
    htmlContent = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
                color: white;
                padding: 10px 0;
                text-align: center;
            }
            nav {
                background-color: #444;
                display: flex;
                justify-content: center;
                padding: 10px;
            }
            nav a {
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                margin: 0 10px;
            }
            nav a:hover {
                background-color: #575757;
            }
            .content {
                padding: 20px;
                text-align: center;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Contact Us</h1>
        </header>
        <nav>
            <a href="/home">Home</a>
            <a href="/about">About</a>
            <a href="/services">Services</a>
            <a href="/contact">Contact</a>
        </nav>
        <div class="content">
            <h2>Get in Touch</h2>
            <p>Have any questions or feedback? Reach out to us via email or phone. We're here to help!</p>
        </div>
        <footer>
            <p>&copy; 2024 My Website. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(htmlContent)
