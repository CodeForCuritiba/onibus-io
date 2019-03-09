<!DOCTYPE html>
<html lang="en">
  <head>
    <title>op</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<?php





$myData = array();

if (($handle = fopen('sta-felicidade.csv', "r")) !== FALSE) {
  while(($data = fgetcsv($handle, 400, ",")) !== FALSE) {
      $myData[] = $data;
  }
}



$num = count($myData);

//var_dump($myData);
for ($c=1; $c < $num; $c++) {
  $horario = montaHorarioHTML($myData[$c][3]);
  echo $horario . "<br />\n";
}

function montaHorarioHTML($val) {
  $horario = 
  return $horario;
}
?>
</body>
</html>
