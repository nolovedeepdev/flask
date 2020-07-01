$(document).ready(function()
{
    $("img").on("click", function(event)
    {
        var x = event.pageX - this.offsetLeft;
        var y = event.pageY - this.offsetTop;
        console.log('y: ' + y + ', x: ' + x);
    });
});