function calculate() {
    const input = document.getElementById('numberInput').value;
    const resultDiv = document.getElementById('result');
    
    if (input === "") {
        resultDiv.innerHTML = "Введи число!";
        return;
    }

    const num = Number(input);
    
    resultDiv.innerHTML = `
        Квадрат: ${num ** 2} <br>
        Куб: ${num ** 3} <br>
        Залишок від ділення на 5: ${num % 5}
    `;
}