<?php 

class Calc{
    public function add($val1, $val2){
        return $val1 + $val2;
    }
}

$calc = new Calc();
echo $calc->add(10, 200);
?>