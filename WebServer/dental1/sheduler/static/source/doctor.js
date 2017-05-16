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
	loadDoctors: function(doctorSelected){
        toolDoctorJs.functionResponse = toolDoctorJs.responseDoctors;
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
                toolDoctorJs.functionResponse(data, doctorSelected);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Doctor - Error en la respuesta JSON");
            }
        });
    }
}