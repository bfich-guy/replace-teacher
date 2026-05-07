import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const name = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.authNameInput);
    const password = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.authPasswordInput);
    let status = "";

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

        const nameValue = name.value;
        const passwordValue = password.value;

        const nameValueAndPasswordValueAreNotNull = (nameValue && passwordValue)

        if (nameValueAndPasswordValueAreNotNull) {
            fetch(configRegistry.ENDPOINTS.auth, {
                headers: {"Content-type": "application/json"},
                method: "POST",
                body: JSON.stringify({
                    auth_type: configRegistry.AUTH.TYPE.sign_up,
                    file_path: configRegistry.DATABASE.users,
                    user_db_data: {
                        name: nameValue || null,
                        password: passwordValue || null,
                        status: status || null, 
                    }
                })
            })
            .then(response => response.json())
            .then(responseData => {
                const userId = responseData.user_id;
                const userStatus = responseData.user_status;

                localStorage.setItem(configRegistry.WIDGETS.METHODOLOGIC_PAGE.USER_INFO.userId, userId);
                localStorage.setItem(configRegistry.WIDGETS.METHODOLOGIC_PAGE.USER_INFO.userStatus, userStatus);

                window.location.href = "/methodologic";
            })
        }
    });
})