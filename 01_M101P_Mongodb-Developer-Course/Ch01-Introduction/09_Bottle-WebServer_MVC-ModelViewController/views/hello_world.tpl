<!DOCTYPE hml>
<html>
<head>
<title>Hello World!</title>
<!-- NOTE: Comments can not be after Python code or get error -->
</head>
<body>
<p>
Welcome {{username}} <!-- double-curlys are Python substitution logic telling the template processor that within is a Python variable or expression to be evaluated -->
<p>
<ul> <!-- create a bulleted list using the array from hello_world.py -->
<!-- Python code within HTML-doc to iterate through list of things passed into this template. Bottle allows python code within HTML by using the percent sign indicating what follows is Python. Within HTML, python code does not rely on indentation.  Python code after % -->
%for thing in things:
<li>{{thing}}</li>
%end
<!-- HTML <li> code with Python substitution logic where variable 'thing' is substituted for the string 'thing' -->
<!-- This 'hack' always needed because there is no indentation telling Python the code block is complete -->
</ul><p>
<form action="/favorite_fruit" method="POST">
What is your favorite fruit?
<input type="text" name="fruit" size="40" value=""><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
