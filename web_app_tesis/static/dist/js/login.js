  $('#txtUser').keyup(function () {
  
    let nombre = $('#txtUser').val();
  
    if (nombre == '') {
      $('#alert_lg_User').show();
      $('#alert_lg_User_text').text('Este campo es obligatorio.');
  
    } else {
      $('#alert_lg_User').hide();
    }
  
  })
  
  $('#txtPass').keyup(function () {
  
    let pass = $('#txtPass').val();
  
    if (pass == '') {
      $('#alert_lg_Pass').show();
      $('#alert_lg_Pass_text').text('Este campo es obligatorio.');
  
    }else {
      $('#alert_lg_Pass').hide();
      $('#btningresar').prop('disabled', false);
    }
  
  })


  