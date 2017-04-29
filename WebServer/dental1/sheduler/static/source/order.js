var toolOrderJs= {
	functionResponseGet: null,
    updateOrderEdit: function(idOrder){

        var strDoctor = document.getElementById("inputDoctor").value;
        var strProcedure = document.getElementById("inputProcedure").value;
        var strStation = document.getElementById("inputStation").value;

        var date_in_format = document.getElementById("datepickerIn").value+"T00:00:00-0700";
        var date_out_format = null;
        if($("#datepickerOut").datepicker("getDate") != "Invalid Date"){
            date_out_format =document.getElementById("datepickerOut").value+"T00:00:00-0700";
        }

        var due_date_format = null;
        if($("#datepickerDue").datepicker("getDate") != "Invalid Date"){
            due_date_format =document.getElementById("datepickerDue").value+"T00:00:00-0700";
        }
        if(
            strDoctor == null ||
            date_in_format == null ||
            strProcedure == null ||
            document.getElementById("inputCase").value == "" ||
            document.getElementById("inputPatient").value == "" ||
            document.getElementById("inputCost").value == "" ||
            document.getElementById("inputDescription").value == ""
            ){
                alert("Falta diligenciar  información de la sección")
        }
        else
        {
            var objectOrder = {
                "case": document.getElementById("inputCase").value,
                "patient": document.getElementById("inputPatient").value,
                "description": document.getElementById("inputDescription").value,
                "doctor": strDoctor,
                "procedure": strProcedure,
                "date_in" : date_in_format,
                "due_date" : due_date_format,
                "date_out" : date_out_format,
                "station" : strStation,
                "cost" : document.getElementById("inputCost").value
            }
            // console.log(JSON.stringify(objectOrder));
            // alert("almacenando");
            toolOrderJs.requestPUT('/sheduler/orders/'+idOrder+'/',objectOrder);
        }
    },
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
        if(document.getElementById("inputCase").value == ""
            || strDoctor == null ||
            document.getElementById("inputPatient").value == "" || date_in_format == null
            || document.getElementById("inputCost").value == "" || strProcedure == null ||
            document.getElementById("inputDescription").value == ""
            ){
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
            // console.log(JSON.stringify(objectOrder));
            // alert("almacenando");
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

            // $('#listProcedures').val(data.procedure);
            // $('#listProcedures').selectpicker('refresh');

            // $('#listDoctors').val(data.doctor);
            // $('#listDoctors').selectpicker('refresh');

            // $('#listStations').val(data.station);
            // $('#listStations').selectpicker('refresh');


            $('#inputProcedure').val(data.procedure);
            $('#inputDoctor').val(data.doctor);
            $('#inputStation').val(data.station);


            $('#inputPatient').val(data.patient);
            $('#inputCase').val(data.case);
            $('#inputDescription').val(data.description);

            $('#datepickerIn').datepicker('setDate', new Date(data.date_in));

            if(data.date_out!=null)
                $('#datepickerOut').datepicker('setDate', new Date(data.date_out));
            if(data.due_date!=null)
                $('#datepickerDue').datepicker('setDate', new Date(data.due_date));

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
                    window.location = "/sheduler/index/";
                 },
                 error: function (xhr) {
                    console.log(xhr.responseText);
                    alert("Order saved -- JSON");
                 }
             });
    },
}