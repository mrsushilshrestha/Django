from django.http import HttpResponse

def about(request):
    myhtml = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Me</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                background-color: #f4f4f4;
                color: #333;
                padding: 0 20px;
            }

            header {
                background-color: #007bff;
                color: white;
                padding: 10px 0;
                text-align: center;
            }

            header nav {
                margin: 0 10px;
                font-size: 1.2em;
                cursor: pointer;
            }

            header nav:hover {
                text-decoration: underline;
            }

            section {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin: 20px 0;
                padding: 20px;
                background-color: white;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }

            .container {
                text-align: center;
                max-width: 800px;
            }

            .container img {
                max-width: 100%;
                height: auto;
                border-radius: 8px;
                margin-top: 20px;
            }

            .container p {
                margin: 20px 0;
                font-size: 1.1em;
            }

            footer {
                text-align: center;
                margin-top: 20px;
                padding: 10px;
                background-color: #007bff;
                color: white;
                font-size: 0.9em;
            }
            p {
            text-align: justify;
        }
        </style>
    </head>
    <body>
        <header>
            <nav><a href="/about">About Me</a></nav>
            <nav><a href="/contact">Contact</a></nav>
        </header>

        <section>
            <div class="container">
                <p>My name is Sushil Shrestha, a passionate technology enthusiast and Python developer from Nepal. I am currently pursuing a Bachelor's degree in Information Technology at Himalayan WhiteHouse International College. With a deep interest in coding and technology, I have honed my skills in Python, ethical hacking, and various programming concepts. My goal is to leverage my knowledge and skills to innovate and solve real-world problems, particularly in the fields of software development and cybersecurity. I actively engage in coding challenges, projects, and collaborations to keep expanding my expertise.</p>
                <img src="https://img-cdn.pixlr.com/image-generator/history/65bb506dcb310754719cf81f/ede935de-1138-4f66-8ed7-44bd16efc709/medium.webp" alt="My Photo">
            </div>
        </section>

        <footer>
            &copy; 2025 Sushil Shrestha. All Rights Reserved.
        </footer>
    </body>
    </html>
    """
    return HttpResponse(myhtml)

def contact(request):
    contactHtml=""""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            padding: 0 20px;
        }

        header {
            background-color: #007bff;
            color: white;
            padding: 10px 0;
            text-align: center;
        }

        header nav {
            margin: 0 10px;
            font-size: 1.2em;
            cursor: pointer;
        }

        header nav:hover {
            text-decoration: underline;
        }

        section {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px 0;
            padding: 20px;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            max-width: 600px;
            margin: 20px auto;
        }

        .container {
            text-align: center;
        }

        .container input, .container textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ddd;
        }

        .container button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .container button:hover {
            background-color: #0056b3;
        }

        footer {
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            background-color: #007bff;
            color: white;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<header>
    <nav><a href="/about">About Me</a></nav>
    <nav><a href="/contact">Contact</a></nav>
</header>

<section>
    <div class="container">
        <h2>Contact Us</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="Your Name" required><br>
            <input type="email" name="email" placeholder="Your Email" required><br>
            <textarea name="message" placeholder="Your Message" rows="5" required></textarea><br>
            <button type="submit">Submit</button>
        </form>
    </div>
</section>

<footer>
    &copy; 2025 Sushil Shrestha. All Rights Reserved.
</footer>

</body>
</html>

    """
    return HttpResponse(contactHtml)
