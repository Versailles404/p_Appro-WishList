<?php
include("../../controller/metDataBase.php");
include("../../controller/metLogin.php");
//include("../../controller")

?>

<!DOCTYPE html>
<head>
    <style href="../css/style.css"></style>
</head>
<body>

    <h1>
        WishList
    </h1>

    <ul>
        <li>Mes wishlists
        <li>Partagé avec moi 
        </li>
    </ul>
    <div class="newAdded">
        <h2>
            Derniers ajouts
        </h2>
        <table>
        <tr class="headerList">
            <th>Nom
            <th>Prix
            <th>Utilisateur
            <th>Liste
            </th>
          </tr>
        <?php
        /*foreach(product in products)
        {
            $html .= "<tr>";
            $html .= "<td>";
            $html .= "</td>";
            $html .= "</tr>";
            echo $html;
        }*/
        ?>
          
        </table>
    </div>
    

    <div>
        <h3>
            À propos
        </h3>
        <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut aliquam purus sit amet luctus. Amet mattis vulputate enim nulla aliquet porttitor lacus. Nisl rhoncus mattis rhoncus 
        urna neque viverra justo nec. Proin gravida hendrerit lectus a. Est ante in nibh mauris cursus mattis molestie a. Bibendum 
        ut tristique et egestas quis ipsum suspendisse ultrices. Purus faucibus ornare suspendisse sed nisi lacus. Nisl pretium 
        fusce id velit ut tortor pretium viverra suspendisse. Tempus imperdiet nulla malesuada pellentesque elit eget gravida cum. 
        Quis imperdiet massa tincidunt nunc pulvinar sapien. Et leo duis ut diam quam nulla porttitor massa id. Sit amet est placerat 
        in egestas erat imperdiet. Sit amet mattis vulputate enim nulla aliquet. Suspendisse potenti nullam ac tortor vitae purus 
        faucibus ornare. Mauris rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Ac turpis egestas 
        integer eget aliquet. Quam lacus suspendisse faucibus interdum posuere lorem ipsum dolor.
        </p>
    </div>
    

</body>
</html>