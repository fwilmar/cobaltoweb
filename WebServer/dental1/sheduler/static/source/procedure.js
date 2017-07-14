var toolProcedureJs= {
	functionResponseGet: null,
    createProcedure: function(){
        toolProcedureJs.functionResponseGet = toolProcedureJs.createProcedureInfo;
        if(document.getElementById("inputNewProcedure").value == ""){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectProcedure = {
                "name": document.getElementById("inputNewProcedure").value,
            }
        }
             // console.log(JSON.stringify(objectProcedure));
             // alert("almacenando");
             // alert(JSON.stringify(objectProcedure));
        toolProcedureJs.requestPost("/sheduler/procedures/",objectProcedure);
    },
    readProcedure: function(idProcedure) {
        toolProcedureJs.functionResponseGet = toolProcedureJs.readProcedureInfo;
        toolProcedureJs.requestRest('/sheduler/procedures/'+idProcedure);
    },
    updateProcedure: function(idProcedure){
        console.log(idProcedure);
        toolProcedureJs.functionResponseGet = toolProcedureJs.updateProcedureInfo;
        if(document.getElementById("inputProcedureName").value == ""){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectProcedure = {
                "name": document.getElementById("inputProcedureName").value,
            }
        }
        toolProcedureJs.requestPUT('/sheduler/procedures/'+idProcedure+'/',objectProcedure);
    },
    deleteProcedure: function(idProcedure){
        toolProcedureJs.functionResponseGet = toolProcedureJs.deleteProcedureInfo;
        toolProcedureJs.requestDelete('/sheduler/procedures/'+idProcedure+'/');
    },
    createProcedureInfo: function(data){
        $('#SaveModal').modal('hide');
        $('#confirmModal').modal('show');
    },
    readProcedureInfo: function(data, procedureSelected){
        $('#inputProcedureName').val(data.name);
    },
    updateProcedureInfo: function(data){
        $('#SaveModal').modal('hide');
        $('#confirmModal').modal('show');
    },
    deleteProcedureInfo: function(data){
        $('#DeleteModal').modal('hide');
        $('#confirmModal').modal('show');
    },



	loadProcedures: function(procedureSelected){
        toolProcedureJs.functionResponseGet = toolProcedureJs.responseProcedures;
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
                toolProcedureJs.functionResponseGet(data, procedureSelected);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error en la respuesta JSON");
            }
        });
    },
    requestPost: function(urlRest, objectProcedure) {
            $.ajax({
                 type: "POST",
                 url: urlRest,
                 data: JSON.stringify(objectProcedure),
                 contentType: "application/json; charset=utf-8",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolProcedureJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr, status, thrownError) {
                    toolProcedureJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    },
    requestPUT: function(urlRest, objectProcedure) {
             // alert(JSON.stringify(objectProcedure));
            $.ajax({
                 type: "PUT",
                 url: urlRest,
                 data: JSON.stringify(objectProcedure),
                 contentType: "application/json; charset=utf-8",
                 // dataType: "json",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolProcedureJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr, status, thrownError) {
                    // toolProcedureJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    },
    requestDelete: function(urlRest) {
            $.ajax({
                 type: "DELETE",
                 url: urlRest,
                 contentType: "application/json; charset=utf-8",
                 dataType: "json",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolProcedureJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr) {
                    toolProcedureJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    }
}