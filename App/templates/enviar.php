<?php

if(isset($_POST["enviar"])){
    $nombre=$_POST["nombre"];
    $email=$_POST["email"];
    $mensaje=$_POST["mensaje"];
    $telefono=$_POST["telefono"];

    $destinatario="renzocifro@gmail.com";
    $asunto="nuevo mensaje de $email";

    $contenido="Nombre: $nombre \n";
    $contenido.="EMail: $email \n";
    $contenido.="telefono: $telefono \n"
    $contenido.="Mensaje: $mensaje ";
    
    $header="From: Aviso de Mail";

    $mail=mail($destinatario,$asunto,$contenido,$header);

    if($mail){
        echo "<script>alert('El correo se envio correctamente')</script>"
    }else{
        echo "<script>alert('El correo se envio correctamente')</script>"
    }
}
?>