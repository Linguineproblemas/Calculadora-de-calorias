function CalcularCalorais() {
     const checkboxes = document.querySelectorAll('.food:checked');
            let totalCalorias = 0;
            checkboxes.forEach(checkbox => {
                totalCalorias += parseInt(checkbox.value);
            });
            document.getElementById('resultado').innerText = `Total de Calorias: ${totalCalorias} Kcal`;
        }
