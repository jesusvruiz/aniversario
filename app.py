from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template_string("""

<!DOCTYPE html>
<html lang="es">

<head>
                                  <link rel="preconnect" href="https://fonts.googleapis.com">

<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<meta charset="UTF-8">
<title>Nuestro Aniversario ❤️</title>

<style>

/* FONDO GENERAL */

body{
    margin:0;
    padding:0;
    overflow:hidden;
    font-family: 'Poppins', sans-serif;

    background: linear-gradient(180deg,#050816,#0b1026,#1a1f3d);

    height:100vh;

    display:flex;
    justify-content:center;
    align-items:center;
}

/* ESTRELLAS */

.stars{
    position:fixed;

    width:100%;
    height:100%;

    background-image:
        radial-gradient(white 1px, transparent 1px),
        radial-gradient(white 1px, transparent 1px),
        radial-gradient(white 2px, transparent 2px);

    background-size:
        120px 120px,
        200px 200px,
        300px 300px;

    background-position:
        0 0,
        40px 60px,
        130px 270px;

    animation: moverEstrellas 30s linear infinite;

    opacity:0.7;
}

/* LUNA */

.moon{

    position:fixed;

    top:60px;
    right:80px;

    width:120px;
    height:120px;

    background:#f5f3ce;

    border-radius:50%;

    box-shadow:
        0 0 40px #fff8b0,
        0 0 80px rgba(255,255,255,0.3);

    z-index:1;
}

/* TARJETA */

.card{

    position:relative;

    z-index:2;

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(10px);

    padding:40px;

    border-radius:30px;

    text-align:center;

    width:80%;
    max-width:700px;

    color:white;

    box-shadow:
        0 10px 40px rgba(0,0,0,0.5),
        0 0 25px rgba(255,255,255,0.15);

    animation: aparecer 2s ease;
}

/* FOTO */

img{

    width:220px;
    height:220px;

    object-fit:cover;

    border-radius:20px;

    border:5px solid white;

    margin-bottom:20px;
}

/* TITULO */

h1{
                                  font-family: 'Dancing Script', cursive;
    font-size:50px;

    margin:10px;
}

/* TEXTO */

p{

    font-size:22px;

    line-height:1.6;
}

/* BOTONES */

button{

    padding:15px 30px;

    border:none;

    border-radius:15px;

    background:#ff4d6d;

    color:white;

    font-size:18px;

    cursor:pointer;

    margin-top:20px;

    transition:0.3s;
}

button:hover{

    background:#ff1744;

    transform:scale(1.05);
}

/* ANIMACION TARJETA */

@keyframes aparecer{

    from{
        opacity:0;
        transform:translateY(50px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* CORAZONES */

.heart{

    position:absolute;

    color:white;

    animation: caer linear infinite;
}

@keyframes caer{

    0%{
        transform:translateY(-100px);
        opacity:1;
    }

    100%{
        transform:translateY(100vh);
        opacity:0;
    }
}

/* SOBRE Y FONDO */

#fondoCarta{

    position:fixed;

    top:0;
    left:0;

    width:100%;
    height:100%;

    background:rgba(0,0,0,0.85);

    display:none;

    justify-content:center;
    align-items:center;
    flex-direction:column;

    z-index:999;
}

/* SOBRE */

#sobre{

    font-size:120px;

    cursor:pointer;

    animation: flotar 2s infinite ease-in-out;
}

/* CARTA */

#carta{
font-family: 'Poppins', sans-serif;
    display:none;

    background:white;

    color:#333;

    width:80%;
    max-width:650px;

    padding:30px;

    border-radius:25px;

    text-align:center;

    animation: aparecerCarta 1s ease;
}

/* ANIMACION SOBRE */

@keyframes flotar{

    0%{
        transform:translateY(0px);
    }

    50%{
        transform:translateY(-10px);
    }

    100%{
        transform:translateY(0px);
    }
}

/* ANIMACION CARTA */

@keyframes aparecerCarta{

    from{
        opacity:0;
        transform:scale(0.8);
    }

    to{
        opacity:1;
        transform:scale(1);
    }
}

/* ESTRELLAS MOVIMIENTO */

@keyframes moverEstrellas{

    from{
        transform:translateY(0px);
    }

    to{
        transform:translateY(200px);
    }
}
/* BOTON CERRAR */

#cerrar{

    position:absolute;

    top:20px;
    right:20px;

    background:#ff1744;

    width:45px;
    height:45px;

    border-radius:50%;

    padding:0;

    font-size:20px;
}
</style>
</head>

<body>

<!-- ESTRELLAS -->

<div class="stars"></div>

<!-- LUNA -->

<div class="moon"></div>

<!-- MUSICA -->

<audio id="musica" loop>
    <source src="/static/musica.mp3" type="audio/mpeg">
</audio>

<!-- CORAZONES -->

<div class="heart" style="left:10%; animation-duration:6s; font-size:30px;">❤️</div>

<div class="heart" style="left:20%; animation-duration:8s; font-size:25px;">❤️</div>

<div class="heart" style="left:35%; animation-duration:7s; font-size:35px;">❤️</div>

<div class="heart" style="left:50%; animation-duration:5s; font-size:20px;">❤️</div>

<div class="heart" style="left:70%; animation-duration:9s; font-size:40px;">❤️</div>

<div class="heart" style="left:85%; animation-duration:6s; font-size:28px;">❤️</div>

<!-- TARJETA -->

<div class="card">

    <img src="/static/foto.jpg">

    <h1>Feliz Aniversario ❤️</h1>

    <p>
        Gracias por existir y llenar mi vida de felicidad.
        Cada momento contigo se convierte en mi recuerdo favorito.
    </p>

    <p id="contador"></p>

    <button onclick="abrirCarta()">
        Abrir Carta 💌
    </button>

    <br><br>

    <button onclick="reproducirMusica()">
        🎵 Reproducir Nuestra Canción
    </button>

</div>

<!-- SOBRE -->

<div id="fondoCarta">

    <div id="sobre" onclick="mostrarMensaje()">
        ✉️
    </div>

    <!-- CARTA -->

    <div id="carta">
<button onclick="cerrarCarta()" id="cerrar">
    ✖
</button>
        <h2 style="font-family: 'Dancing Script', cursive;
font-size:45px; color:#ff4d6d;">

Mi caprichosa ❤️

</h2>

        <p>
            Feliz aniversario, 8 años y 3 meses
            (por si te hayas olvidado 😡)
        </p>

        <p>
            Decirte que amo cada cosa de ti.
            Sin duda alguna, eres el amor de mi vida.
        </p>

        <p>
            Hemos pasado por muchas cosas,
            y a pesar de todo seguimos juntos.
        </p>

        <p>
            Definitivamente quiero pasar mi vida entera contigo,
            hasta de viejitos como nos decíamos al inicio.
        </p>

        <p>
            ¡TE AMOOOO HASTA LA LUNA
            EN PASITOS DE TORTUGA 😍❤️!
        </p>

    </div>

</div>

<script>

/* CONTADOR */

function actualizarTiempo(){

    document.getElementById("contador").innerHTML =
    "Llevamos juntos 8 años y 3 meses ❤️";
}

setInterval(actualizarTiempo,1000);

/* MUSICA */

function reproducirMusica(){

    const musica = document.getElementById("musica");

    musica.play();
}

/* ABRIR SOBRE */

function abrirCarta(){

    document.getElementById("fondoCarta").style.display = "flex";
}

/* MOSTRAR CARTA */

function mostrarMensaje(){

    document.getElementById("sobre").style.display = "none";

    document.getElementById("carta").style.display = "block";
}
/* CERRAR CARTA */

function cerrarCarta(){

    document.getElementById("fondoCarta").style.display = "none";

    document.getElementById("sobre").style.display = "block";

    document.getElementById("carta").style.display = "none";
}
</script>

</body>
</html>

""")

if __name__ == "__main__":
    app.run(debug=True)