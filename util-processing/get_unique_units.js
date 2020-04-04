const readline = require('readline');

// const unitMap = JSON.parse('{"TFT2_Aatrox":0,"TFT2_Amumu":1,"TFT2_Annie":2,"TFT2_Ashe":3,"TFT2_Azir":4,"TFT2_Brand":5,"TFT2_Braum":6,"TFT2_Diana":7,"TFT2_DrMundo":8,"TFT2_Ezreal":9,"TFT2_Ivern":10,"TFT2_Janna":11,"TFT2_Jax":12,"TFT2_Karma":13,"TFT2_Khazix":14,"TFT2_Kindred":15,"TFT2_KogMaw":16,"TFT2_LeBlanc":17,"TFT2_Leona":18,"TFT2_Lucian":19,"TFT2_LuxCrystal":20,"TFT2_LuxElectric":21,"TFT2_LuxGlacial":22,"TFT2_LuxInferno":23,"TFT2_LuxLight":24,"TFT2_LuxMetal":25,"TFT2_LuxOcean":26,"TFT2_LuxShadow":27,"TFT2_LuxWind":28,"TFT2_LuxWoodland":29,"TFT2_Malphite":30,"TFT2_Malzahar":31,"TFT2_Maokai":32,"TFT2_MasterYi":33,"TFT2_Nami":34,"TFT2_Nasus":35,"TFT2_Nautilus":36,"TFT2_Neeko":37,"TFT2_Nocturne":38,"TFT2_Olaf":39,"TFT2_Ornn":40,"TFT2_QiyanaInferno":41,"TFT2_QiyanaOcean":42,"TFT2_QiyanaWind":43,"TFT2_QiyanaWoodland":44,"TFT2_RekSai":45,"TFT2_Renekton":46,"TFT2_Senna":47,"TFT2_Singed":48,"TFT2_Sion":49,"TFT2_Sivir":50,"TFT2_Skarner":51,"TFT2_Soraka":52,"TFT2_Syndra":53,"TFT2_Taliyah":54,"TFT2_Taric":55,"TFT2_Thresh":56,"TFT2_Twitch":57,"TFT2_Varus":58,"TFT2_Vayne":59,"TFT2_Veigar":60,"TFT2_Vladimir":61,"TFT2_Volibear":62,"TFT2_Warwick":63,"TFT2_Yasuo":64,"TFT2_Yorick":65,"TFT2_Zed":66,"TFT2_Zyra":67}');
// const unitMapLength = 68;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

let s = new Set();
let num_lines = 0;
rl.on('line', (line) => {
    num_lines++;
    // console.log(line);
    const obj = JSON.parse(line);
    const { game_datetime } = obj.info;

    for(let i=0;i<8;i++){
        const { units, placement } = obj.info.participants[i];
        for(let u of units) s.add(u.character_id);
    }
});

rl.on('close', () => {
    console.log(`${num_lines} lines read`);

    const unitArr = [...s];
    unitArr.sort();

    const map = {};
    for(let i = 0; i != unitArr.length; i++){
        map[unitArr[i]] = i;
    }
    console.log(JSON.stringify(map));

    for (let u of unitArr)
      console.log(u);
    console.log(unitArr.length);
});