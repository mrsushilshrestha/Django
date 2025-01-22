from django.http import HttpResponse

from django.shortcuts import render


def about(request):
    
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
