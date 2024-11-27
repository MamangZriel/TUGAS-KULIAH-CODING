
function hitungKomisi() {
    const pendapatan = parseFloat(document.getElementById('pendapatan').value);
    let uangJasa = 0;
    let komisi = 0;

    if (pendapatan <= 200000) {
    uangJasa = 10000;
    komisi = 0.1 * pendapatan;
    } else if (pendapatan <= 500000) {
    uangJasa = 20000;
    komisi = 0.15 * pendapatan;
    } else {
    uangJasa = 30000;
    komisi = 0.2 * pendapatan;
}

    const total = uangJasa + komisi;

    document.getElementById('hasil').innerText = 
`Pendapatan: Rp ${pendapatan.toLocaleString()}
    \nUang Jasa: Rp ${uangJasa.toLocaleString()}
    \nKomisi: Rp ${komisi.toLocaleString()}
    \nTotal Pendapatan: Rp ${total.toLocaleString()}`;
}
