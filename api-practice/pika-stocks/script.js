

async function getData() {
    const response = await fetch('https://api.pikastocks.com/prints/22512/prices');
    const data = await response.json();
    console.log(data);
}