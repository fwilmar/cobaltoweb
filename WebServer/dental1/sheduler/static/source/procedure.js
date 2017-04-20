var toolProcedureJs= {
	functionResponse: null,
	loadProcedures: function(schedule){
        toolProcedureJs.functionResponse = toolProcedureJs.responseProcedures;
        toolProcedureJs.requestRest('/sheduler/procedures');
    },
	responseProcedures: function(data){
		var options;
        for (var i = 0; i < data['length']; i++) {
            options += "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
        }
        $('#listProcedures').append(options);
        $('#listProcedures').selectpicker('refresh');
    },
	requestRest: function(urlRest) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolProcedureJs.functionResponse(data);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error en la respuesta JSON");
            }
        });
    }
}