<!DOCTYPE html>
<html>
<head>
	<title>log in</title>
	
	
</head>
<body style="background-image: url(gaming.jpg);
background-repeat: no-repeat;
background-size: cover;
   background-color: #cccccc;">


<form action="/check" method="post">
<h1 style ="text-align: center; color: white; ">Leitað af highscore</h1>
<h2 style ="position:  fixed; top: 7.5%; right: 53.6%; color: white; " >Nafn:</h2>
<input style ="position:  fixed; top: 10%; right: 43.2%; " type="text" name="nafn" required=""><br>
<button  style ="position:  fixed; top: 10%; right: 43.2%;" name="Leita"  type="submit">leita</button><br>
</form>

<form  style ="position:  fixed; top: 13%; right: 53.8%;" action="/all">
	<button name="baka" type="submit">sjá allt</button>
</form>

</body>
