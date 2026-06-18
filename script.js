function vergleichen () {
    const preisPackungA = Number(document.getElementById("packungA").value);
    const anzahlRollenA = Number(document.getElementById("rollenA").value);
    const blattanzahlA = Number(document.getElementById("blattanzahlA").value);
    const preisPackungB = Number(document.getElementById("packungB").value);
    const anzahlRollenB = Number(document.getElementById("rollenB").value);
    const blattanzahlB = Number(document.getElementById("blattanzahlB").value);

    const anzahlBlattGesamtA = anzahlRollenA * blattanzahlA
    const kostenProBlattA = preisPackungA / anzahlBlattGesamtA

    const anzahlBlattGesamtB = anzahlRollenB * blattanzahlB
    const kostenProBlattB = preisPackungB / anzahlBlattGesamtB

    let fazit = "";
    if (kostenProBlattA < kostenProBlattB) {
        fazit = "<strong>Fazit: Packung A ist günstiger!</strong>";
    }   
    else {
        fazit = "<strong>Fazit: Packung B ist günstiger!</strong>";
    }

    let ersparnis = "";
    if (kostenProBlattA < kostenProBlattB) {
        ersparnis = kostenProBlattB - kostenProBlattA;
    }
    else {
        ersparnis = kostenProBlattA - kostenProBlattB
    }
    
    document.getElementById("ergebnis").innerHTML = "Packung A kostet " + kostenProBlattA.toFixed(4) + " € pro Blatt.<br>" + "Packung B kostet " + kostenProBlattB.toFixed(4) + " € pro Blatt.<br><br>" + fazit + "<br><br>" + "Ersparnis pro Blatt: " + ersparnis.toFixed(4) + " €";

    
}

function menuOeffnen() {
    document
    .getElementById("menu")
    .classList
    .toggle("sichtbar");
}
