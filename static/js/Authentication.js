import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const name = document.getElementById(configRegistry.WIDGETS.INPUTS.authNameInput);
    const password = document.getElementById(configRegistry.WIDGETS.INPUTS.authPasswordInput);
    let status = "";

    const setStudentStatusButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.setStudentStatusButton);
    const setTeacherStatusButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.setTeacherStatusButton);
    const signUpButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.signUpButton);

    setStudentStatusButton.addEventListener("click", function() {
        status = configRegistry.AUTH.USER_STATUS.student;
    });

    setTeacherStatusButton.addEventListener("click", function() {
        status = configRegistry.AUTH.USER_STATUS.teacher;
    });

    signUpButton.addEventListener("click", function() {

        const nameValue = name.value;
        const passwordValue = password.value;

        const nameValueAndPasswordValueAreNotNull = (nameValue && passwordValue)

        if (nameValueAndPasswordValueAreNotNull) {
            fetch(authEndpoint, {
                headers: {"Content-type": "application/json"},
                method: "POST",
                body: JSON.stringify({
                    auth_type: configRegistry.AUTH.TYPE.sign_up,
                    file_path: configRegistry.DATABASE.users,
                    user_data: {
                        name: nameValue || null,
                        password: passwordValue || null,
                        status: status || null, 
                    }
                })
            })
        }
    });
})