<?php 
    session_start();    
    session_destroy();
    echo "<center>";
    echo "<h1>成功登出</h1>";
    echo "</center>";
    header("Refresh:1; url=login.php");
?>