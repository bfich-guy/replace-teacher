import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    let status = "";

    const signUpNameInput = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.signUpNameInput);
    const signUpPasswordInput = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.signUpPasswordInput);

    const setStudentStatusButton = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.BUTTONS.setStudentStatusButton);
    const setTeacherStatusButton = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.BUTTONS.setTeacherStatusButton);
    const signUpButton = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.BUTTONS.signUpButton);

    setStudentStatusButton.addEventListener("click", function() {
        status = configRegistry.AUTH.USER_STATUS.student;
    });

    setTeacherStatusButton.addEventListener("click", function() {
        status = configRegistry.AUTH.USER_STATUS.teacher;
    });

    signUpButton.addEventListener("click", function() {

        const signUpNameValue = signUpNameInput.value;
        const signUpPasswordValue = signUpPasswordInput.value;

        const signUpDataIsNotNull = (signUpNameValue && signUpPasswordValue)

        if (signUpDataIsNotNull) 
        {
            fetch(configRegistry.ENDPOINTS.signUpEndpoint, 
            {
                headers: {"Content-type": "application/json"},
                method: "POST",
                body: JSON.stringify({
                    auth_type: configRegistry.AUTH.TYPE.sign_up,
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
                const userId = responseData.user_id;
                const userStatus = responseData.user_status;

                window.location.href = configRegistry.ENDPOINTS.methodologicEndpoint;
            })
        }
    });
})