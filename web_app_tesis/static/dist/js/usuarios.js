codHCL();

function codHCL() {
    let num = 5
    const characters = '1234567890';
    let codigo = '';
    const charactersLength = characters.length;
    for (let i = 0; i < num; i++) {
        codigo += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    document.getElementById('txtHistorialC').value = 'HSTR-' + codigo
}

function validaNumericos(event) {
    if (event.charCode >= 48 && event.charCode <= 57) {
        return true;
    }
    return false;
}

const selectElementAnio = document.querySelector('#txtanio');
selectElementAnio.addEventListener('change', (event) => {
    var currentTime = new Date();
    let anio = document.getElementById('txtanio').value;
    let edad = currentTime.getFullYear() - anio
    document.getElementById('txtEdad').value = edad;
});

document.querySelector('#customCheckbox6').addEventListener('click', () => {
    document.querySelector('#txtarea').disabled = false;
    document.querySelector('#co_txtareas').innerText = 'Ingrese otras observaciones'
});

const selectElementDni = document.querySelector('#txtdni');
selectElementDni.addEventListener('change', (event) => {
    fetch('http://127.0.0.1:8000/validar_dni/?dni=' + selectElementDni.value, {
        method: 'GET',
    }).then((data) => {
        if (data.ok == true) {
            toastr.error('El paciente con este DNI ya está registrado!')
            selectElementDni.value = ''
        }
    })
});
const selectElementTelefono = document.querySelector('#txttelef');
selectElementTelefono.addEventListener('change', (event) => {
    fetch('http://127.0.0.1:8000/validar_telef/?tel=' + selectElementTelefono.value, {
        method: 'GET',
    }).then((data) => {
        if (data.ok == true) {
            toastr.error('El paciente con este Teléfono ya está registrado!')
            selectElementTelefono.value = ''
        }
    })
});
var selec = [];

function registro_p() {
    let historia = document.getElementById('txtHistorialC').value;
    let dni = document.getElementById('txtdni').value;
    let nombre = document.getElementById('txtnom01').value + ' ' + document.getElementById('txtnom02').value
    let apellidos = document.getElementById('txtape01').value + ' ' + document.getElementById('txtape02').value
    let nombre_completo = nombre + ' ' + apellidos
    let edad = document.getElementById('txtEdad').value;
    let tel = document.getElementById('txttelef').value;
    let medico_id = JSON.parse(localStorage.getItem('datos')).id_usuario;
    let genero = document.getElementById('txtgenero').value;

    let gestante = document.getElementById("customCheckbox1").checked
    let Diabetes = document.getElementById("customCheckbox2").checked
    let Hipertensión = document.getElementById("customCheckbox3").checked
    let PCoagulación = document.getElementById("customCheckbox4").checked
    let Alergico = document.getElementById("customCheckbox5").checked
    let otros = document.getElementById("customCheckbox6").checked

    if (dni == '' && document.getElementById('txtnom01').value == '' && document.getElementById('txtape01').value == '' && document.getElementById('txtape02').value == '' && document.getElementById('txtdia').value == '' && document.getElementById('txtanio').value == '' && tel == '') {

        document.querySelector('#co_dni').innerText = 'Este campo es obligatorio';
        document.querySelector('#co_nom').innerText = 'Este campo es obligatorio';
        document.querySelector('#co_ap01').innerText = 'Este campo es obligatorio';
        document.querySelector('#co_ap02').innerText = 'Este campo es obligatorio';
        document.querySelector('#co_dia').innerText = 'Este campo es obligatorio';
        document.querySelector('#co_anio').innerText = 'Este campo es obligatorio';
        document.querySelector('#co_tel').innerText = 'Este campo es obligatorio';

    } else if (dni == '' || document.getElementById('txtnom01').value == '' || document.getElementById('txtape01').value == '' || document.getElementById('txtape02').value == '' || document.getElementById('txtdia').value == '' || document.getElementById('txtanio').value == '' || tel == '') {

        if (dni == '') {
            document.querySelector('#co_dni').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_dni').innerText = '';
        }

        if (document.getElementById('txtnom01').value == '') {
            document.querySelector('#co_nom').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_nom').innerText = '';
        }

        if (document.getElementById('txtape01').value == '') {
            document.querySelector('#co_ap01').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_ap01').innerText = '';
        }

        if (document.getElementById('txtape02').value == '') {
            document.querySelector('#co_ap02').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_ap02').innerText = '';
        }

        if (document.getElementById('txtdia').value == '') {
            document.querySelector('#co_dia').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_dia').innerText = '';
        }

        if (document.getElementById('txtanio').value == '') {
            document.querySelector('#co_anio').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_anio').innerText = '';
        }

        if (tel == '') {
            document.querySelector('#co_tel').innerText = 'Este campo es obligatorio';
        } else {
            document.querySelector('#co_tel').innerText = '';
        }
    } else {
        document.querySelector('#co_dni').innerText = '';
        document.querySelector('#co_nom').innerText = '';
        document.querySelector('#co_ap01').innerText = '';
        document.querySelector('#co_ap02').innerText = '';
        document.querySelector('#co_dia').innerText = '';
        document.querySelector('#co_anio').innerText = '';
        document.querySelector('#co_tel').innerText = '';
        if (gestante) {
            selec.push('Gestante')
            console.log('gestante esta seleccionado');
        }
        if (Diabetes) {
            selec.push('Diabetes')
        }
        if (Hipertensión) {
            selec.push('Hipertensión')
        }
        if (PCoagulación) {
            selec.push('PCoagulación')
        }
        if (Alergico) {
            selec.push('Alergico')
        }
        if (otros) {
            selec.push(document.getElementById('txtarea').value)
        }

        if (selec.length > 0) {

            let obs = 'El paciente padece de ' + selec

            Swal.fire({
                title: '<strong>PACIENTE con observaciones</strong>',
                text: "You won't be able to revert this!",
                icon: 'info',
                html: 'El paciente padece de <b>' + selec + '</b>',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '<i class="fa fa-thumbs-up"></i> Confirmar Registro!',
                cancelButtonText: 'No, cancelar!',
            }).then((result) => {
                if (result.isConfirmed) {

                    fetch('http://127.0.0.1:8000/registrar_paciente/?hist=' + historia + '&dni=' + dni + '&nombre_apellidos=' + nombre_completo + '&genero=' + genero + '&telefono=' + tel + '&edad=' + edad + '&id_medico_tratante_id=' + medico_id + '&observaciones=' + obs, {
                        method: 'GET',
                    }).then((data) => {
                        dni.value = ''
                        nombre_completo.value = ''
                        edad.value = ''
                        tel.value = ''
                        document.getElementById('txtdni').value = ''
                        document.getElementById('txtanio').value = ''
                        Swal.fire({
                            position: 'top-center',
                            icon: 'success',
                            title: 'Paciente registrado con éxito!',
                            showConfirmButton: false,
                            timer: 1500
                        }).then(function () {
                            location.href = "../historial_pacientes"
                        });
                    })
                } else if (
                    result.dismiss === Swal.DismissReason.cancel
                ) {
                    Swal.fire({
                        position: 'top-center',
                        icon: 'error',
                        title: 'Cancelado!',
                        showConfirmButton: false,
                        timer: 1500
                    }).then(function () {
                        location.href = "../historial_pacientes"
                    });
                }
            })

        } else {
            let obs = 'Sin observaciones';
            fetch('http://127.0.0.1:8000/registrar_paciente/?hist=' + historia + '&dni=' + dni + '&nombre_apellidos=' + nombre_completo + '&genero=' + genero + '&telefono=' + tel + '&edad=' + edad + '&id_medico_tratante_id=' + medico_id+ '&observaciones=' + obs, {
                method: 'GET',
            }).then((data) => {
                dni.value = ''
                nombre_completo.value = ''
                edad.value = ''
                tel.value = ''
                document.getElementById('txtdni').value = ''
                document.getElementById('txtanio').value = ''
                Swal.fire({
                    position: 'top-center',
                    icon: 'success',
                    title: 'Paciente registrado con éxito!',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () {
                    location.href = "../historial_pacientes"
                });
            })

        }










    }




}