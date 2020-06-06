const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

canvas.width = 500;
canvas.height = 500;

ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 150, 100);