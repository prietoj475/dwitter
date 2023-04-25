<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Dwitter: A Twitter-like App built with Django</h1>
    <p>Dwitter is a simple Twitter-like web application built with Django, designed to allow users to share and read short messages called "dweets".</p>
    <img src="https://github.com/prietoj475/dwitter/blob/main/dwitterdemo.png" alt="Dwitter Preview">
    <h2>Features</h2>
    <ul>
      <li>User registration and login</li>
      <li>User profiles</li>
      <li>Ability to create, and read messsages</li>
      <li>Ability to follow and unfollow other users</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
      <li>Python 3.6 or later</li>
      <li>Django 3.1 or later</li>
    </ul>
    <h2>Installation and Usage</h2>
    <ol>
      <li>Clone the repository:</li>
    </ol>
    <pre><code>git clone https://github.com/prietoj475/dwitter.git</code></pre>
    <ol start="2">
      <li>Install the dependencies:</li>
    </ol>
    <pre><code>cd dwitter
pip install -r requirements.txt</code></pre>
    <ol start="3">
      <li>Apply migrations:</li>
    </ol>
    <pre><code>python manage.py migrate</code></pre>
    <ol start="4">
      <li>Run the development server:</li>
    </ol>
    <pre><code>python manage.py runserver</code></pre>
    <ol start="5">
      <li>Open <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> in your browser to access the app.</li>
    </ol>
    <h2>Contributing</h2>
    <p>Contributions are welcome! If you'd like to contribute to this project, please follow these steps:</p>
    <ol>
      <li>Fork the repository</li>
      <li>Create a new branch with your feature or bug fix</li>
      <li>Make your changes and commit them</li>
      <li>Push your changes to your fork</li>
      <li>Create a pull request</li>
    </ol>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>
