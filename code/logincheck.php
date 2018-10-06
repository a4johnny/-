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
        //echo $aa."<br>".$bb;
        $link = mysqli_connect("127.0.0.1","","","test") or die("no");
        mysqli_query($link,"SET NAMES 'utf8' ");

        $sql = "SELECT * from `user` ";
        $result = mysqli_query($link,$sql);

        $state = 0;
        while($row = mysqli_fetch_row($result))
        {
            if($aa == $row[1] && $bb == $row[2]){
                $state = 1;
                echo "<center>";
                echo "<h1>登入成功</h1>";
                echo "</center>";
                $_SESSION['now']=$row[1];
                header("Refresh:1; url=show.php");
            }
            else if($aa == $row[1] && $bb != $row[2]){
                $state = 1;
                echo "<center>";
                echo "<h1>密碼錯誤</h1>";
                echo "</center>";
                header("Refresh:1; url=login.php");
            }
        }

        if ($state == 0){
            echo "<center>";
            echo "<h1>帳號不存在</h1>";
            echo "</center>";
            header("Refresh:1; url=login.php");
        }

    ?>
</body>
</html>