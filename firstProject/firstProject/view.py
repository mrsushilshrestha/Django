from django.contrib import admin
from django.urls import path
from django.http import HttpResponse 

from django.shortcuts import render


def about(request):
<<<<<<< HEAD
    html="""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/about">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/contact">Contact</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>

    <marquee direction="right"><h1>Hello, world From About!</h1></marquee>

    <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://img.lazcdn.com/us/domino/7a8b0a91-6966-4dea-84e3-bc1bcd384fa6_NP-1976-688.jpg_2200x2200q80.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="https://img.lazcdn.com/us/domino/449a0f6a-3283-4cf7-a9cc-b6f368fd652e_NP-1976-688.jpg_2200x2200q80.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="https://img.lazcdn.com/us/domino/fdcd7bd7-41cc-4318-b929-6ab65e3f11e3_NP-1976-688.jpg_2200x2200q80.jpg" class="d-block w-100" alt="...">
    </div>
        <div class="carousel-item">
      <img src="https://img.lazcdn.com/us/domino/5f1ef282-3dc5-4729-8493-6340fcd7d612_NP-1976-688.jpg_2200x2200q80.jpg" alt="...">
    </div>    <div class="carousel-item">
      <img src="https://img.lazcdn.com/us/domino/1e04145a-435e-4049-9120-673165b6244c_NP-1976-688.jpg_2200x2200q80.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
  
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>


"""
    return HttpResponse(html)
def contact(request):
    html="""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/about">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/contact">Contact</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>

    <h1>Hello, world From contact!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>"""

    return HttpResponse(html)
=======
    
    return render(request,"about.html")

# def contact(request):
#     contactHtml=""""
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Contact Us</title>
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         body {
#             font-family: Arial, sans-serif;
#             line-height: 1.6;
#             background-color: #f4f4f4;
#             color: #333;
#             padding: 0 20px;
#         }

#         header {
#             background-color: #007bff;
#             color: white;
#             padding: 10px 0;
#             text-align: center;
#         }

#         header nav {
#             margin: 0 10px;
#             font-size: 1.2em;
#             cursor: pointer;
#         }

#         header nav:hover {
#             text-decoration: underline;
#         }

#         section {
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             margin: 20px 0;
#             padding: 20px;
#             background-color: white;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             border-radius: 8px;
#             max-width: 600px;
#             margin: 20px auto;
#         }

#         .container {
#             text-align: center;
#         }

#         .container input, .container textarea {
#             width: 100%;
#             padding: 10px;
#             margin: 10px 0;
#             border-radius: 5px;
#             border: 1px solid #ddd;
#         }

#         .container button {
#             padding: 10px 20px;
#             background-color: #007bff;
#             color: white;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }

#         .container button:hover {
#             background-color: #0056b3;
#         }

#         footer {
#             text-align: center;
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #007bff;
#             color: white;
#             font-size: 0.9em;
#         }
#     </style>
# </head>
# <body>

# <header>
#     <nav><a href="/about">About Me</a></nav>
#     <nav><a href="/contact">Contact</a></nav>
# </header>

# <section>
#     <div class="container">
#         <h2>Contact Us</h2>
#         <form method="POST">
#             <input type="text" name="name" placeholder="Your Name" required><br>
#             <input type="email" name="email" placeholder="Your Email" required><br>
#             <textarea name="message" placeholder="Your Message" rows="5" required></textarea><br>
#             <button type="submit">Submit</button>
#         </form>
#     </div>
# </section>

# <footer>
#     &copy; 2025 Sushil Shrestha. All Rights Reserved.
# </footer>

# </body>
# </html>

#     """
#     return HttpResponse(contactHtml)

def contact(request):
    
    return render(request,"contact.html")

def daraz(request):
    return render(request,"index.html")
>>>>>>> refs/remotes/origin/main
