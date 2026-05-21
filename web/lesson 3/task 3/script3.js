const colors = ["red", "blue", "green", "yellow", "purple"];
let currentIndex = 0;

const btn = document.getElementById('colorBtn');

btn.addEventListener('click', () => {
    document.body.style.backgroundColor = colors[currentIndex];
    
    currentIndex = (currentIndex + 1) % colors.length;
});