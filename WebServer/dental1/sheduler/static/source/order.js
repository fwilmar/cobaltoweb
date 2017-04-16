var toolOrderJs= {
	functionResponse: null,
    day:null,
    schedule:null,
    saveOrder: function(){
        var e = document.getElementById("listDoctors");
        var strDoctor = e.options[e.selectedIndex].value;
        e = document.getElementById("listProcedures");
        var strProcedure = e.options[e.selectedIndex].value;
        e = document.getElementById("listStations");
        var strStation = e.options[e.selectedIndex].value;
        var date_in_format = document.getElementById("datepickerIn").value+"T00:00:00-0700";
        var date_out_format = document.getElementById("datepickerOut").value+"T00:00:00-0700";
        if(document.getElementById("inputCase").value == "" || strDoctor == null ||
            document.getElementById("inputPatient").value == "" || date_in_format == null
            || document.getElementById("inputCost").value == "" || strProcedure == null ||
            document.getElementById("inputDescription").value == "" || date_out_format == null){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectOrder = {
                "case": document.getElementById("inputCase").value,
                "doctor": strDoctor,
                "patient": document.getElementById("inputPatient").value,
                "procedure": strProcedure,
                "description": strStation,
                "date_in" : date_in_format,
                "date_out" : date_out_format,
                "statin" : document.getElementById("inputPatient").value,
                "cost" : document.getElementById("inputCost").value
            }
            toolOrderJs.requestPost("/sheduler/createorder/",objectOrder);
        }
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
                    alert('Order saved');
                 },
                 error: function (xhr) {
                     alert("Error en la respuesta JSON");
                 }
             });
    }
}