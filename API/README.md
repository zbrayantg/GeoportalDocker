# Documentación de la API

### Endpoints
Consultar todos los predios registrados en el sistema
```
http://bif-env.eba-rbkeuhmg.us-west-2.elasticbeanstalk.com//api/properties
```

### Metodos
Por el momento solo se permite un metodo GET y este se encarga de consultar todos los predios registrados en el sistema.

### Response
```
export interface PropertiesResponse {
    predial:             string;
    alternative_predial: string;
    appraisal:           string;
    document_type:       string;
    act:                 string;
    document_number:     string;
    real_state_register: string;
    document_date:       Date;
    coordenates:         string;
    file:                null;
    status:              Status;
    licence:             Licence;
    occupancy:           Occupancy;
}

export interface Licence {
    curation:          string;
    modality:          string;
    type_construction: string;
    licence_number:    string;
    licence_date:      null;
    construction_date: null;
    area:              number;
}

export interface Occupancy {
    owner:              string;
    contract:           string;
    type_occupancy:     string;
    id_document:        string;
    ocuppancy_document: string;
    ocuppancy_name:     string;
    seppi:              string;
    observation:        string;
}

export interface Status {
    number:         string;
    category:       string;
    type_property:  string;
    name:           string;
    video:          null;
    addres:         string;
    class_property: string;
    use:            string;
}

```

### Headers
No se requiere ningun header

### Body
No se requiere ningun body

### Params
No se requiere ningun parametro
