var data_points = document.getElementById('data_to_map').value;
var list_markers = JSON.parse(data_points);
var map = L.map('map',{maxZoom: 19, minZoom: 12}).setView([7.086927157235266, -73.10079574584962],13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 19,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiemJndWFsZHJvbiIsImEiOiJjbDByYm92M2QwMXdpM2lrM2EzbHlyZmxiIn0.XGfJ3J3kuet2WLnWTFMTkg'
}).addTo(map);
//Se permite escalar el mapa
L.control.scale().addTo(map);



layerGroup = new L.LayerGroup().addTo(map);

const create_bindpopup_content = (data) => {
  let container = document.createElement('div');

  //ID
  let did_id = document.createElement('div');
  did_id.classList.add('mt-2', 'mb-1');
  let did_id_label = document.createElement('p');
  did_id_label.classList.add('m-0');
  did_id_label.innerHTML = 'Identificador: ';
  let did_id_value = document.createElement('p');
  did_id_value.classList.add('m-0');
  did_id_value.innerHTML = data.id;
  did_id.appendChild(did_id_label);
  did_id.appendChild(did_id_value);
  container.appendChild(did_id);

  // Predial
  let predial = document.createElement('div');
  predial.classList.add('mt-1','mb-1');
  let predial_label = document.createElement('p');
  predial_label.classList.add('m-0');
  predial_label.innerHTML = 'Predial: ';
  let predial_text = document.createElement('p');
  predial_text.classList.add('m-0');
  data.predial?predial_text.innerHTML = data.predial: predial_text.innerHTML = 'No registra';
  predial.appendChild(predial_label);
  predial.appendChild(predial_text);
  container.appendChild(predial);

  // Matricula
  let real_register = document.createElement('div');
  real_register.classList.add('mt-1','mb-1');
  let real_register_label = document.createElement('p');
  real_register_label.classList.add('m-0');
  real_register_label.innerHTML = 'Matricula Inmobiliaria: ';
  let real_register_text = document.createElement('p');
  real_register_text.classList.add('m-0');
  data.real_register?real_register_text.innerHTML = data.real_register: real_register_text.innerHTML = 'No registra';
  real_register.appendChild(real_register_label);
  real_register.appendChild(real_register_text);
  container.appendChild(real_register);

  //Tipo de ocupacion
  let occupancy = document.createElement('div');
  occupancy.classList.add('mt-1','mb-1');
  let occupancy_label = document.createElement('p');
  occupancy_label.classList.add('m-0');
  occupancy_label.innerHTML = 'Tipo ocupación: ';
  let occupancy_text = document.createElement('p');
  occupancy_text.classList.add('m-0');
  data.occupancy?occupancy_text.innerHTML = data.occupancy: occupancy_text.innerHTML = 'No registra';
  occupancy.appendChild(occupancy_label);
  occupancy.appendChild(occupancy_text);
  container.appendChild(occupancy);

  //Ocupante
  let name_occupancy = document.createElement('div');
  name_occupancy.classList.add('mt-1','mb-1');
  let name_occupancy_label = document.createElement('p');
  name_occupancy_label.classList.add('m-0');
  name_occupancy_label.innerHTML = 'Nombre del ocupante: ';
  let name_occupancy_text = document.createElement('p');
  name_occupancy_text.classList.add('m-0');
  data.name_occupancy?name_occupancy_text.innerHTML = data.name_occupancy: name_occupancy_text.innerHTML = 'No registra';
  name_occupancy.appendChild(name_occupancy_label);
  name_occupancy.appendChild(name_occupancy_text);
  container.appendChild(name_occupancy);

  //video
  if(data.video){
    let video = document.createElement('div');
    video.classList.add('text-center','mb-2','mt-1');
    let video_btn_show = document.createElement('a');
    video_btn_show.innerHTML = 'Ver video';
    //video_btn_show.addEventListener('click', show_video(data.video));
    video_btn_show.setAttribute('href', data.video);
    video_btn_show.setAttribute('target', '_blank');
    video.appendChild(video_btn_show);
    container.appendChild(video);
  }

  return container;
}

/*
//Funcion para mostrar el video
const show_video = (video) => {
  if(video)return console.log(video);
}*/

//Agregar marcadores
let list_error_polygon = [];
for (const [key, value] of Object.entries(list_markers)) {
    if(key == "1") console.log(value);
    try{
      let poligono = {
        "type": "FeatureCollection",
        "features": [
          {
            "type": "Feature",
            "properties": {
              "OBJECTID": key,
              "PREDIAL": value.predial
            },
            "geometry": {
              "type": "MultiPolygon",
              "coordinates": JSON.parse(value.coordenadas) 
            }
          }]
      }
      let new_pol = L.geoJson(poligono).bindPopup(create_bindpopup_content(value))
      layerGroup.addLayer(new_pol);
    }
    catch(err){
      //list_error_polygon.push(value.id);
    }
  }
  //console.log(list_error_polygon);
  /*var latlng = L.latLng(value.latitud, value.longitud);
    marker = new L.Marker(latlng, { draggable: false, title:value.nombre, alt:"Resource Location", riseOnHover:true}).addTo(map);
    marker.bindPopup("EL PREDIO ES PROPIEDAD DE <b>"+value.propietario + "</b> <br> PERTENECE AL SECTOR <b>"+value.sector+"</b><br> UBICADO EN <b>"+value.direccion+"</b>"+ "<br>").addTo(map); 
  } */


/*   map.on('click', mapClicked);
        
  function mapClicked(e) {
      //Agregar el marcador
      marker = new L.Marker(e.latlng, { draggable: true, title:"Resource location", alt:"Resource Location", riseOnHover:true });
      marker.bindPopup("Ubicación seleccionada").addTo(map).openPopup();
      console.log(e.latlng.lat,e.latlng.lng);
  }
 */
/* const container_table = document.getElementById('table_body')
for (poligono of poligonos.features) {
  let row = document.createElement('tr')
  let td_predial = document.createElement('td')
  let td_coordenates = document.createElement('td')
  row.appendChild(td_predial)
  row.appendChild(td_coordenates)
  container_table.appendChild(row)
  td_predial.innerHTML = poligono.properties.NUM_PRED
  //td_coordenates.innerHTML = poligono.properties.AREA_TOT
  td_coordenates.innerHTML = JSON.stringify(poligono.geometry.coordinates)
  //let polygon = poligono.geometry.coordinates
  //console.log(JSON.stringify(polygon))
} */

/* 
console.log("------------------------------------------------------")
console.log(poligonos.features[0].geometry.coordinates) */