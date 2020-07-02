//AJAX that get coordinates
let barra = [];
let xlist = []; let ylist = []; // array para colocar os eixos
let totalWH = [];

var myCanvas = document.getElementById("myCanvas");
var ctx = myCanvas.getContext("2d");
myCanvas.width = 500;
myCanvas.height = 500;

$(document).ready(function() {
    $("img").on("click", function (event) {
        const x = event.pageX - this.offsetLeft; // pega o x
        const y = event.pageY - this.offsetTop; // pega o y
        var cw = this.clientWidth; // Avalia o tamanho da imagem
        var ch = this.clientHeight;

        totalWH.push(cw, ch);


        xlist.push(x); ylist.push(y);

        let auxw = xlist.length;
        let auxh = ylist.length;

        if (auxw && auxh === 2){
            if (xlist[1] >= xlist[0] && ylist[1] >= ylist[0]){
                const w = xlist[1] - xlist[0]; // se o index 1 do lista x for maior, w = xlist[1] - xlist[0]
                const h = ylist[1] - ylist[0]; // se o index 1 do lista y for maior, h = ylist[1] - ylist[0]
                const fx = xlist[0]; const fy = ylist[0]

                ctx.fillStyle = "#ffc107", "#6200ea", "#304ffe", "#33691e", "#ff6f00";
                ctx.fillRect(fx, fy, w, h);

                barra.push(fx, fy, w, h);
                xlist = []; ylist = []
                console.log(`x: ${fx}, y: ${fy}, w: ${w}, h: ${h} -> ${barra} `)

            }
            else {
                const w = xlist[0] - xlist[1];
                const h = ylist[0] - ylist[1];
                const fx = xlist[1]; const fy = ylist[1]
                barra.push(fx, fy, w, h);
                console.log(`x: ${fx}, y: ${fy}, w: ${w}, h: ${h} -> ${barra}`)
                xlist = []; ylist = []

                const json = {

                };
            };
        };
    });
});

