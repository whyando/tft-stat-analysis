var x = `
[ 3.76647834e-04  8.09792844e-03  1.69491525e-03  7.72128060e-03
    4.19962335e-02  3.76647834e-04  1.22222222e-01  1.12994350e-03
    9.53860640e-01  1.36346516e-01  3.76647834e-04  3.63465160e-02
    7.96610169e-01  1.37476460e-01  5.02636535e-01  4.70809793e-03
    2.46704331e-02  2.07156309e-03  5.27306968e-03  3.76647834e-04
    4.33145009e-03  5.78154426e-02  5.57438795e-02  1.88323917e-04
    1.88323917e-04  7.53295669e-04  1.31826742e-03  4.33145009e-03
    4.42561205e-02 -4.98732999e-18  1.52542373e-02  7.53295669e-04
    3.76647834e-04  2.20338983e-02  3.70998117e-02  2.63653484e-03
    1.31826742e-03  5.64971751e-04  7.15630885e-03  9.78531073e-01
    1.76647834e-01  6.96798493e-03  6.21468927e-03  1.01694915e-02
    9.98116761e-03  3.95480226e-03  9.12052731e-01  1.88323917e-03
    2.87947269e-01  9.23728814e-01  1.35593220e-02  2.25988701e-03
    2.10922787e-02 -6.70297151e-15  1.88323917e-04  5.14124294e-02
    5.64971751e-04  2.40112994e-01  1.69491525e-03  5.64971751e-04
    5.64971751e-04  5.64971751e-04  9.90395480e-01  2.29755179e-02
    2.63653484e-03  5.27306968e-03  2.42749529e-01  5.64971751e-04]
`
x = x.replace(/[\[\]]/g,'');
x = x.replace(/\s+/g,' ').trim();
x = x.split(/\s+/);
console.log(x);


const unitMap = JSON.parse('{"TFT2_Aatrox":0,"TFT2_Amumu":1,"TFT2_Annie":2,"TFT2_Ashe":3,"TFT2_Azir":4,"TFT2_Brand":5,"TFT2_Braum":6,"TFT2_Diana":7,"TFT2_DrMundo":8,"TFT2_Ezreal":9,"TFT2_Ivern":10,"TFT2_Janna":11,"TFT2_Jax":12,"TFT2_Karma":13,"TFT2_Khazix":14,"TFT2_Kindred":15,"TFT2_KogMaw":16,"TFT2_LeBlanc":17,"TFT2_Leona":18,"TFT2_Lucian":19,"TFT2_LuxCrystal":20,"TFT2_LuxElectric":21,"TFT2_LuxGlacial":22,"TFT2_LuxInferno":23,"TFT2_LuxLight":24,"TFT2_LuxMetal":25,"TFT2_LuxOcean":26,"TFT2_LuxShadow":27,"TFT2_LuxWind":28,"TFT2_LuxWoodland":29,"TFT2_Malphite":30,"TFT2_Malzahar":31,"TFT2_Maokai":32,"TFT2_MasterYi":33,"TFT2_Nami":34,"TFT2_Nasus":35,"TFT2_Nautilus":36,"TFT2_Neeko":37,"TFT2_Nocturne":38,"TFT2_Olaf":39,"TFT2_Ornn":40,"TFT2_QiyanaInferno":41,"TFT2_QiyanaOcean":42,"TFT2_QiyanaWind":43,"TFT2_QiyanaWoodland":44,"TFT2_RekSai":45,"TFT2_Renekton":46,"TFT2_Senna":47,"TFT2_Singed":48,"TFT2_Sion":49,"TFT2_Sivir":50,"TFT2_Skarner":51,"TFT2_Soraka":52,"TFT2_Syndra":53,"TFT2_Taliyah":54,"TFT2_Taric":55,"TFT2_Thresh":56,"TFT2_Twitch":57,"TFT2_Varus":58,"TFT2_Vayne":59,"TFT2_Veigar":60,"TFT2_Vladimir":61,"TFT2_Volibear":62,"TFT2_Warwick":63,"TFT2_Yasuo":64,"TFT2_Yorick":65,"TFT2_Zed":66,"TFT2_Zyra":67}');
const unitMapLength = 68;
const unitMapRev = [];

const pair_arr = [];

for(k in unitMap){
    const i = unitMap[k];
    pair_arr.push({unit: k, weight: x[i]});
}
pair_arr.sort((a,b) => b.weight - a.weight);

for(let i = 0; i != 10; i++){
    console.log(`${pair_arr[i].unit}\t${(+pair_arr[i].weight).toFixed(2)}`);
}