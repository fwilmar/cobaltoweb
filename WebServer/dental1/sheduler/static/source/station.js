var toolStationJs= {
	functionResponse: null,
	loadStations: function(schedule){
        toolStationJs.functionResponse = toolStationJs.responseStations;
        toolStationJs.requestRest('/sheduler/stations');
    },
	responseStations: function(data){
		var options;
        for (var i = 0; i < data['length']; i++) {
            options += "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
        }
        $("#listStations").append(options);
        $('#listStations').selectpicker('refresh');
    },
	requestRest: function(urlRest) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolStationJs.functionResponse(data);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error en la respuesta JSON");
            }
        });
    }
}