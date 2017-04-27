var toolOrderJs= {
	functionResponseGet: null,
    day:null,
    schedule:null,
    updateOrder: function(idOrder){
        toolOrderJs.buildOrder('upadte',idOrder);
    },
    saveOrder: function(){
        toolOrderJs.buildOrder('save',0);
    },
    buildOrder: function(action, idOrder){
        var e = document.getElementById("listDoctors");
        var strDoctor = e.options[e.selectedIndex].value;
        e = document.getElementById("listProcedures");
        var strProcedure = e.options[e.selectedIndex].value;
        e = document.getElementById("listStations");
        var strStation = e.options[e.selectedIndex].value;
        var date_in_format = document.getElementById("datepickerIn").value+"T00:00:00-0700";
        var date_out_format = null;
        console.log($("#datepickerOut").datepicker("getDate"));
        if($("#datepickerOut").datepicker("getDate") != "Invalid Date"){
            date_out_format =document.getElementById("datepickerOut").value+"T00:00:00-0700";
        }
        var due_date_format = null;
        console.log($("#datepickerDue").datepicker("getDate"));
        if($("#datepickerDue").datepicker("getDate") != "Invalid Date"){
            due_date_format =document.getElementById("datepickerDue").value+"T00:00:00-0700";
        }
        if(document.getElementById("inputCase").value == "" || strDoctor == null ||
            document.getElementById("inputPatient").value == "" || date_in_format == null
            || document.getElementById("inputCost").value == "" || strProcedure == null ||
            document.getElementById("inputDescription").value == ""){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectOrder = {
                "case": document.getElementById("inputCase").value,
                "doctor": strDoctor,
                "patient": document.getElementById("inputPatient").value,
                "procedure": strProcedure,
                "description": document.getElementById("inputDescription").value,
                "date_in" : date_in_format,
                "due_date" : due_date_format,
                "date_out" : date_out_format,
                "station" : strStation,
                "cost" : document.getElementById("inputCost").value
            }
            console.log(JSON.stringify(objectOrder));
            alert("almacenando");
            if(action=="save"){
                toolOrderJs.requestPost("/sheduler/orders/",objectOrder);
            }else{
                toolOrderJs.requestPUT('/sheduler/orders/'+idOrder+'/',objectOrder);
            }


        }
    },
    printOrder: function(action){
        if(document.getElementById("inputCase").value==""){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectOrder = {
                "case": document.getElementById("inputCase").value
            }
            console.log(' -----printOrder--- ');
            toolOrderJs.requestPost("/sheduler/orders/printorder/");
        }
    },
    loadOrder: function(idOrder) {
        toolOrderJs.functionResponseGet = toolOrderJs.responseOrder;
        toolOrderJs.requestRest('/sheduler/orders/'+idOrder);
    },
    responseOrder: function(data){
            $('#inputCase').val(data.case);

            $('#listProcedures').val(data.procedure);
            $('#listProcedures').selectpicker('refresh');

            $('#listDoctors').val(data.doctor);
            $('#listDoctors').selectpicker('refresh');
            $('#inputPatient').val(data.patient);

            $('#inputDescription').val(data.description);
            $('#datepickerIn').val(data.date_in.split('T')[0]);
            if(data.date_out!=null)
                $('#datepickerOut').val(data.date_out.split('T')[0]);
            if(data.due_date!=null)
                $('#datepickerDue').val(data.due_date.split('T')[0]);
            $('#listStations').val(data.station);
            $('#listStations').selectpicker('refresh');
            // $('#listDoctors option:contains('+data.doctor+')').attr('selected', true).trigger('change');
            $('#inputCost').val(data.cost);

    },
    requestRest: function(urlRest) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolOrderJs.functionResponseGet(data);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error en la respuesta JSON");
            }
        });
    },
    requestPUT: function(urlRest, objectOrder) {
            $.ajax({
                 type: "PUT",
                 url: urlRest,
                 data: JSON.stringify(objectOrder),
                 contentType: "application/json; charset=utf-8",
                 dataType: "json",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    alert('Order saved');
                 },
                 error: function (xhr) {
                    console.log(xhr.responseText);
                    alert("Order saved --- JSON");
                 }
             });
    },
    requestPost: function(urlRest, objectOrder) {
            $.ajax({
                 type: "POST",
                 url: urlRest,
                 data: JSON.stringify(objectOrder),
                 contentType: "application/json; charset=utf-8",
                 dataType: "json",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    console.log(data);
                    alert('Order saved');
                 },
                 error: function (xhr) {
                    console.log(xhr.responseText);
                    alert("Order saved -- JSON");
                 }
             });
    },
}