export const configRegistry = {
    AUTH: {
        USER_DATA: {
            name: "name",
            password: "password", 
        },
        USER_STATUS: {
            student: "student",
            teacher: "teacher",
        },
        TYPE: {
            sign_up: "sign_up",
            log_in: "log_in",
        },
    },
    DATABASE: {
        users: "database/users.json",
    },
    ENDPOINTS: {
        index: "/",
        auth: "/auth",
        methodologic: "/methodologic",
    },
    WIDGETS: {
        INDEX_PAGE: {
            INPUTS: {
                authNameInput: "auth-name-input",
                authPasswordInput: "auth-password-input",
            },
            BUTTONS: {
                setStudentStatusButton: "set-student-status-button",
                setTeacherStatusButton: "set-teacher-status-button",
                signUpButton: "sign-up-button",
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