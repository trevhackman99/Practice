window.onload = function() {
    fetch('formattedData.json')
        .then(response => response.json())
        .then(data => {
            
            // console.log(`${data[0].name} - ${data[0].version}`)
            for (let i = 0; i < data.length; i++) {
                const table = document.getElementById('main-table');
                let row = document.createElement('tr');
                let cell = document.createElement('td');
                cell.textContent = `${data[i].name} - ${data[i].version}`;
                row.appendChild(cell);
                cell = document.createElement('td');
                cell.textContent = data[i].set;
                row.appendChild(cell);
                cell = document.createElement('td');
                cell.textContent = data[i].collector_number;
                row.appendChild(cell);
                cell = document.createElement('td');
                cell.textContent = data[i].rarity;
                row.appendChild(cell);
                cell = document.createElement('td');
                cell.textContent = data[i].normal;
                row.appendChild(cell);
                cell = document.createElement('td');
                cell.textContent = data[i].foil;
                row.appendChild(cell);

                table.appendChild(row);
            }
        }) 
        .catch(error => {
            console.error('Error fetching data:', error);
        }
    );

    
};

