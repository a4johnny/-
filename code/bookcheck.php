<?php 
    session_start();
?>
<html>
<head>
<title>xxxxx</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <?php
        $aa = $_POST['ur'];
        $bb = $_POST['ps'];
        $state = 0;
        //echo $aa."<br>".$bb;
        $link = mysqli_connect("127.0.0.1","","","test") or die("no");
        mysqli_query($link,"SET NAMES 'utf8' ");

        if (strlen($aa)<1 || strlen($bb)<1 ){
            $state = 2;
            echo "<center>";
            echo "<h1>帳號或密碼不可為空</h1>";
            echo "</center>";
            header("Refresh:1; url=book.php");
        }

        $sql = "SELECT * from `user` ";
        $result = mysqli_query($link,$sql);

        if ($state != 2){
            while($row = mysqli_fetch_row($result))
            {
                if($aa == $row[1]){
                        $state = 1;
                        echo "<center>";
                        echo "<h1>帳號重複</h1>";
                        echo "</center>";
                        header("Refresh:1; url=book.php");
                }

            }

            if ($state == 0){
                echo "<center>";
                echo "<h1>申請成功</h1>"."<br>"."<h2>帳號:".$aa."</h2><br>"."<h2>密碼:".$bb."</h2><br>"."<br>";
                echo "<h1>請重新登入</h1>";
                echo "</center>";
                mysqli_query($link, "INSERT INTO `user` (`name`, `password`) VALUES ('$aa' , '$bb' )");
                $_SESSION['now']=$row[1];
                echo "<center>";
                echo "<input type=\"submit\" value=\"確認\" onclick=\"location.href='login.php'\">";
                echo "</center>";
            }
        }
    ?>
</body>
</html>