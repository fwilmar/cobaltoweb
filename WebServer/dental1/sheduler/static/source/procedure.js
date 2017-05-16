var toolProcedureJs= {
	functionResponse: null,
	loadProcedures: function(procedureSelected){
        toolProcedureJs.functionResponse = toolProcedureJs.responseProcedures;
        toolProcedureJs.requestRest('/sheduler/procedures',procedureSelected);
    },
	responseProcedures: function(data, procedureSelected){
		var options;
        for (var i = 0; i < data['length']; i++) {
            options += "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
        }
        $('#listProcedures').append(options);
        if(procedureSelected!=null)
        {
            $('#listProcedures').val(procedureSelected);
        }
        $('#listProcedures').selectpicker('refresh');
    },
	requestRest: function(urlRest, procedureSelected) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolProcedureJs.functionResponse(data, procedureSelected);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error en la respuesta JSON");
            }
        });
    }
}