let isSpinning = false;
let rotationsOuter = -11.25;
let rotationsInner = 0;

function spin() {
    if(isSpinning) return;
            
    isSpinning = true;
    const roulet = document.getElementById('roulet');
            
    const extraRotationsOuter = 4;
    const randomAngleOuter = Math.floor(Math.random() * 360);
    rotationsOuter += extraRotationsOuter * 360 + randomAngleOuter;

    roulet.style.transform = `rotate(${rotationsOuter}deg)`;

    setTimeout(() => {
        isSpinning = false;
        const resultOuter = calculateResult(rotationsOuter, 16);
        alert(`Результаты:\nВнешняя: ${resultOuter}\n`);
    }, 5000);
}

function calculateResult(angle, sectors) {
    const sectorAngle = 360 / sectors;
    const resultIndex = Math.round((360 - angle % 360) / sectorAngle) ;
    return document.querySelectorAll('.roulette-item')[(16 + resultIndex - 4) % 16].textContent;
}