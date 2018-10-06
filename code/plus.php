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
        $ps4 = $_SESSION['ps4'];
        $xone = $_SESSION['xone'];
        $ds = $_SESSION['3ds'];
        $ns = $_SESSION['ns'];
        //echo $aa;
        $link = mysqli_connect("127.0.0.1","","","test") or die("no");
        mysqli_query($link,"SET NAMES 'utf8' ");

        mysqli_query($link, "UPDATE `xxxxx` SET `owner`=CONCAT(`owner`,'$user') WHERE `id` = '$aa';");
        echo "<center>";
        echo "<h1>成功新增</h1>";
        echo "</center>";
        if($_SESSION['ps4']>0){
            echo "<center>";
            echo "<form action=\"ps4s.php\" method=\"post\">";
            echo "<input type=\"submit\" value=\"確認\">";
            echo "<input type='hidden' name='a' value= $ps4>";
            echo "</form>";
            echo "</center>";
            //header("Refresh:1; url=ps4s.php");
        }
        else if($_SESSION['ns']>0){
            echo "<center>";
            echo "<form action=\"nss.php\" method=\"post\">";
            echo "<input type=\"submit\" value=\"確認\">";
            echo "<input type='hidden' name='b' value= $ns>";
            echo "</form>";
            echo "</center>";
            //header("Refresh:1; url=ps4s.php");
        }
        else if($_SESSION['3ds']>0){
            echo "<center>";
            echo "<form action=\"3dss.php\" method=\"post\">";
            echo "<input type=\"submit\" value=\"確認\">";
            echo "<input type='hidden' name='c' value= $ds>";
            echo "</form>";
            echo "</center>";
            //header("Refresh:1; url=ps4s.php");
        }
        else if($_SESSION['xone']>0){
            echo "<center>";
            echo "<form action=\"xones.php\" method=\"post\">";
            echo "<input type=\"submit\" value=\"確認\">";
            echo "<input type='hidden' name='d' value= $xone>";
            echo "</form>";
            echo "</center>";
            //header("Refresh:1; url=ps4s.php");
        }
    ?>
</body>
</html>