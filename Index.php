<!DOCTYPE html >

<html lang = "en">
<body>
<head>

        <title>garage door </title>

</head>

<form method = "post"> 

    <h2>
        <center> press button</center>
     </h2>

        <center>

            <input type = "submit" value="Allow Access" name = "allow" style="background:#3630a3;color:white;" > </input>

</form>

        </center>
        <?php

                if(isset(S.POST["allow"])){

                    system("Python/home/ttebe/Desktop/servo.py");
                    
                }
        ?>

</body>
