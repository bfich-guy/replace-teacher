import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    let status = "";

    const signUpNameInput = document.getElementById(configRegistry.WIDGETS.INPUTS.signUpNameInput);
    const signUpPasswordInput = document.getElementById(configRegistry.WIDGETS.INPUTS.signUpPasswordInput);

    const setStudentStatusButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.setStudentStatusButton);
    const setTeacherStatusButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.setTeacherStatusButton);
    const signUpButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.signUpButton);

    setStudentStatusButton.addEventListener("click", function() {
        status = configRegistry.AUTHENTICATION.USER_STATUS.student;
    });

    setTeacherStatusButton.addEventListener("click", function() {
        status = configRegistry.AUTHENTICATION.USER_STATUS.teacher;
    });

    signUpButton.addEventListener("click", function() {

        const signUpNameValue = signUpNameInput.value;
        const signUpPasswordValue = signUpPasswordInput.value;

        const signUpDataIsNotNull = (signUpNameValue && signUpPasswordValue)

        if (signUpDataIsNotNull) 
        {
            fetch(configRegistry.ENDPOINTS.signUpEndpoint, 
            {
                headers: configRegistry.HEADERS.contentTypeApplicationJSON,
                method: configRegistry.METHODS.POST,
                body: JSON.stringify({
                    endpoint: configRegistry.ENDPOINTS.signUpEndpoint,
                    file_path: configRegistry.DATABASE.users,
                    user_input_data: {
                        name: signUpNameValue || null,
                        password: signUpPasswordValue || null,
                        status: status || null,
                        unique_id: null,
                    }
                })
            })
            .then(response => response.json())
            .then(responseData => {

                window.location.href = configRegistry.ENDPOINTS.methodologicEndpoint;
            })
        }
    });
})