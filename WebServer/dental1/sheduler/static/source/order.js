var toolOrderJs= {
    functionResponseGet: null,


    createOrder: function(){
        toolOrderJs.functionResponseGet = toolOrderJs.createOrderInfo;
        toolOrderJs.buildOrder('create',0);
    },
    readOrder: function(idOrder) {
        toolOrderJs.functionResponseGet = toolOrderJs.readOrderInfo;
        toolOrderJs.requestRest('/sheduler/orders/'+idOrder);
    },
    updateOrder: function(idOrder){
        toolOrderJs.functionResponseGet = toolOrderJs.updateOrderInfo;
        toolOrderJs.buildOrder('upadte',idOrder);
    },
    deleteOrder: function(idOrder){
        toolOrderJs.functionResponseGet = toolOrderJs.deleteOrderInfo;
        toolOrderJs.requestDelete('/sheduler/orders/'+idOrder+'/');
    },




    buildOrder: function(action, idOrder){
        var e = document.getElementById("listDoctors");
        var strDoctor = e.options[e.selectedIndex].value;
        e = document.getElementById("listProcedures");
        var strProcedure = e.options[e.selectedIndex].value;
        e = document.getElementById("listStations");
        var strStation = e.options[e.selectedIndex].value;
        e = document.getElementById("valuePriority");
        var valPriority = e.options[e.selectedIndex].value;

        var momentObj = moment($('#datepickerIn').val());
        var date_in_format = momentObj.format();


        var momentObj = moment($('#datepickerIn').val());
        var date_in_format = momentObj.format();

        var date_out_format = null;
        console.log($("#datepickerOut").datepicker("getDate"));
        if($("#datepickerOut").datepicker("getDate") != "Invalid Date"){
            var momentObj = moment($('#datepickerOut').val());
            var date_out_format = momentObj.format();
        }
        var due_date_format = null;
        console.log($("#datepickerDue").datepicker("getDate"));
        if($("#datepickerDue").datepicker("getDate") != "Invalid Date"){
            var momentObj = moment($('#datepickerDue').val());
            var due_date_format = momentObj.format();
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
                "cost" : document.getElementById("inputCost").value,
                "priority" : valPriority
            }
             // console.log(JSON.stringify(objectOrder));
             // alert("almacenando");
             // alert(JSON.stringify(objectOrder));
            if(action=="create"){
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
    createOrderInfo: function(data){
        $('#SaveModal').modal('hide');
        $('#confirmModal').modal('show');
    },
    readOrderInfo: function(data){
        toolDoctorJs.loadDoctors(data.doctor);
        toolProcedureJs.loadProcedures(data.procedure);
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
        if(data.priority!=null){
            $('#valuePriority').val(data.priority);
        }else{
            $('#valuePriority').val(3);
        }
        $('#valuePriority').selectpicker('refresh');
    },
    updateOrderInfo: function(data){
        $('#SaveModal').modal('hide');
        $('#confirmModal').modal('show');
    },
    deleteOrderInfo: function(data){
        $('#DeleteModal').modal('hide');
        $('#confirmModal').modal('show');
    },


    requestRest: function(urlRest) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolOrderJs.functionResponseGet(data);
                console.log(status);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error GET");
            }
        });
    },
    requestPUT: function(urlRest, objectOrder) {
             // alert(JSON.stringify(objectOrder));
            $.ajax({
                 type: "PUT",
                 url: urlRest,
                 data: JSON.stringify(objectOrder),
                 contentType: "application/json; charset=utf-8",
                 // dataType: "json",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolOrderJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr, status, thrownError) {
                    toolOrderJs.functionResponseGet(data);
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
                    toolOrderJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr) {
                    toolOrderJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    },
    requestPost: function(urlRest, objectOrder) {
            $.ajax({
                 type: "POST",
                 url: urlRest,
                 data: JSON.stringify(objectOrder),
                 contentType: "application/json; charset=utf-8",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolOrderJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr, status, thrownError) {
                    toolOrderJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    },
}