function validarMoneda() {
    var moneda = document.getElementById("concepto").value;
    var regex = /^\d+(\.\d{1,2})?$/; // Expresión regular para moneda con hasta 2 decimales
    
    if (regex.test(moneda)) {
        document.getElementById("mensaje").textContent = "Formato de moneda válido: " + moneda;
    } else {
        document.getElementById("mensaje").textContent = "Formato de moneda inválido. Por favor, ingrese un valor válido.";
    }
}