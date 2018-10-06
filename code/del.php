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
        $aa = $_POST['add'];
        $user = $_SESSION['now'];
        //echo $aa;
        $link = mysqli_connect("127.0.0.1","","","test") or die("no");
        mysqli_query($link,"SET NAMES 'utf8' ");

        $sql = "SELECT * from `xxxxx` WHERE `id` = '$aa' ";
        $result = mysqli_query($link,$sql);

        while($row = mysqli_fetch_row($result))
        {
            $str = str_replace($user,"",$row[6]);
            mysqli_query($link, "UPDATE `xxxxx` SET `owner`='$str' WHERE `id` = '$aa';");
            echo "成功刪除";
            header("Refresh:1; url=show.php");
        }
    ?>
</body>
</html>