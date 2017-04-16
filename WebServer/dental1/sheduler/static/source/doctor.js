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
	functionResponse: null,
	loadDoctors: function(schedule){
        toolDoctorJs.functionResponse = toolDoctorJs.responseDoctors;
        toolDoctorJs.requestRest('/sheduler/doctors');
    },
	responseDoctors: function(data){
		var options;
        for (var i = 0; i < data['length']; i++) {
            options += "<option value='"+data[i]['id']+"'>"+data[i]['name']+"</option>";
        }
        $("#listDoctors").append(options);
        $('#listDoctors').selectpicker('refresh');
    },
	requestRest: function(urlRest) {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: urlRest,
            success: function(data) {
                toolDoctorJs.functionResponse(data);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Error en la respuesta JSON");
            }
        });
    }
}