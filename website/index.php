<html>
    <head>
        <title>e-Commerce Site</title>
    </head>

    <body>
        <h1>Welcome to an e-Commerce Platform</h1>
        <ul>
            <?php

            $json = file_get_contents('http://products/');
            $obj = json_decode($json);

            $products = $obj->products;

            foreach ($products as $product) {
                echo "<li>$product</li>";
            }

            ?>
        </ul>
    </body>
</html>