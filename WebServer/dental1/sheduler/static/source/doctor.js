// var csrftoken = $.cookie('csrftoken');
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

var toolDoctorJs= {
	functionResponseGet: null,

    createDoctor: function(){
        toolDoctorJs.functionResponseGet = toolDoctorJs.createDoctorInfo;
        if(document.getElementById("inputNewDoctor").value == ""){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectDoctor = {
                "name": document.getElementById("inputNewDoctor").value,
            }
        }
             // console.log(JSON.stringify(objectDoctor));
             // alert("almacenando");
             // alert(JSON.stringify(objectDoctor));
        toolDoctorJs.requestPost("/sheduler/doctors/",objectDoctor);
    },
    readDoctor: function(idDoctor) {
        toolDoctorJs.functionResponseGet = toolDoctorJs.readDoctorInfo;
        toolDoctorJs.requestRest('/sheduler/doctors/'+idDoctor);
    },
    updateDoctor: function(idDoctor){
        toolDoctorJs.functionResponseGet = toolDoctorJs.updateDoctorInfo;
        if(document.getElementById("inputDoctorName").value == ""){
            alert("Falta diligenciar  información de la sección")
        } else {
            var objectDoctor = {
                "name": document.getElementById("inputDoctorName").value,
            }
        }
        toolDoctorJs.requestPUT('/sheduler/doctors/'+idDoctor+'/',objectDoctor);
    },
    deleteDoctor: function(idDoctor){
        toolDoctorJs.functionResponseGet = toolDoctorJs.deleteDoctorInfo;
        toolDoctorJs.requestDelete('/sheduler/doctors/'+idDoctor+'/');
    },

    createDoctorInfo: function(data){
        $('#SaveModal').modal('hide');
        $('#confirmModal').modal('show');
    },
    readDoctorInfo: function(data, doctorSelected){
        $('#inputDoctorName').val(data.name);
    },
    updateDoctorInfo: function(data){
        $('#SaveModal').modal('hide');
        $('#confirmModal').modal('show');
    },
    deleteDoctorInfo: function(data){
        $('#DeleteModal').modal('hide');
        $('#confirmModal').modal('show');
    },


	loadDoctors: function(doctorSelected){
        toolDoctorJs.functionResponseGet = toolDoctorJs.responseDoctors;
        toolDoctorJs.requestRest('/sheduler/doctors', doctorSelected);
    },
	responseDoctors: function(data, doctorSelected){
		var options;
        for (var i = 0; i < data['length']; i++) {
            options += "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
        }
        $('#listDoctors').append(options);
        if(doctorSelected!=null)
        {
            $('#listDoctors').val(doctorSelected);
        }
        $('#listDoctors').selectpicker('refresh');
    },
	requestRest: function(urlRest, doctorSelected) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolDoctorJs.functionResponseGet(data, doctorSelected);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Doctor - Error en la respuesta JSON");
            }
        });
    },
    requestPost: function(urlRest, objectDoctor) {
            $.ajax({
                 type: "POST",
                 url: urlRest,
                 data: JSON.stringify(objectDoctor),
                 contentType: "application/json; charset=utf-8",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolDoctorJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr, status, thrownError) {
                    toolDoctorJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    },
    requestPUT: function(urlRest, objectDoctor) {
             // alert(JSON.stringify(objectDoctor));
            $.ajax({
                 type: "PUT",
                 url: urlRest,
                 data: JSON.stringify(objectDoctor),
                 contentType: "application/json; charset=utf-8",
                 // dataType: "json",
                 processData: true,
                 success: function (data, status, jqXHR) {
                    toolDoctorJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr, status, thrownError) {
                    // toolDoctorJs.functionResponseGet(data);
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
                    toolDoctorJs.functionResponseGet(data);
                    console.log(status);
                 },
                 error: function (xhr) {
                    toolDoctorJs.functionResponseGet(data);
                    console.log(status);
                 }
             });
    }
}