from rest_framework import serializers
from BIF.models import Property, Status, Licence, Occupancy


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['number', 'category', 'type_property','name','video','addres','class_property','use']

class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        fields = ['curation', 'modality', 'type_construction','licence_number','licence_date','construction_date','area']

class OccupancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupancy
        fields = ['owner', 'contract', 'type_occupancy','id_document','ocuppancy_document','ocuppancy_name','seppi','observation']


class PropertySerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False, read_only=True)
    licence = LicenceSerializer(many=False, read_only=True)
    occupancy = OccupancySerializer(many=False, read_only=True)
    
    class Meta:
        model = Property
        fields = ['predial', 'alternative_predial','appraisal','document_type','act','document_number','real_state_register','document_date','coordenates','file', 'status', 'licence', 'occupancy']