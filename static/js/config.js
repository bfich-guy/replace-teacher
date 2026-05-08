export const configRegistry = {
    AUTH: {
        USER_DATA: {
            name: "name",
            password: "password", 
        },
        USER_STATUS: {
            student: "Ученик",
            teacher: "Учитель",
        },
        TYPE: {
            sign_up: "sign_up",
            log_in: "log_in",
        },
    },
    DATABASE: {
        users: "database/users.json",
    },
    HEADERS: {
        contentTypeApplicationJSON: {"Content-type": "application/json"},
    },
    METHODS: {
        POST: "POST",
    },
    ENDPOINTS: {
        indexEndpoint: "/",
        signUpEndpoint: "/sign_up",
        logInEndpoint: "/log_in",
        methodologicEndpoint: "/methodologic",
    },
    WIDGETS: {
        INDEX_PAGE: {
            INPUTS: {
                signUpNameInput: "sign-up-name-input",
                signUpPasswordInput: "sign-up-password-input",
                logInIdInput: "log-in-id-input",
                logInNameInput: "log-in-name-input",
                logInPasswordInput: "log-in-password-input",
            },
            BUTTONS: {
                setStudentStatusButton: "set-student-status-button",
                setTeacherStatusButton: "set-teacher-status-button",
                signUpButton: "sign-up-button",
                logInButton: "log-in-button",
            },
        },
        METHODOLOGIC_PAGE: {
            TEXTLABELS: {
                userId: "user-id",
                userStatus: "user-status",
            },
            USER_INFO: {
                userId: "user-id",
                userStatus: "user-status",
            },
        },
    },
}