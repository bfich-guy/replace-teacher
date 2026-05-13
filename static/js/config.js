export const configRegistry = {
    AUTHENTICATION: 
    {

        USER_STATUS: 
        {

            student: "Ученик",
            teacher: "Учитель",

        },


    },

    ENDPOINTS: 
    {

        indexEndpoint: "/",
        signUpEndpoint: "/sign_up",
        logInEndpoint: "/log_in",
        mainEndpoint: "/main",
        industrialRoboticsEndpoint: "/industrial_robotics",
        profileEndpoint: "/profile",
        updateProfileEndpoint: "/update_profile",
        deleteProfileEndpoint: "/delete_profile",
        aboutEndpoint: "/about",

    },

    HEADERS: 
    {

        contentTypeApplicationJSON: {"Content-type": "application/json"},

    },

    METHODS: 
    {

        GET: "GET",
        POST: "POST",

    },

    WIDGETS: 
    {

        BUTTONS: 
        {

            setStudentStatusButton: "set-student-status-button",
            setTeacherStatusButton: "set-teacher-status-button",
            signUpButton: "sign-up-button",
            logInButton: "log-in-button",

            industrialRoboticsRedirectButton: "industrial-robotics-redirect-button",
                
            profileRedirectButton: "profile-redirect-button",
            profileUpdateButton: "profile-update-button",
            profileDeleteButton: "profile-delete-button",
            aboutRedirectButton: "about-redirect-button",

            mainRedirectButton: "main-redirect-button",
            
        },

        INPUTS:
        {

            signUpNameInput: "sign-up-name-input",
            signUpPasswordInput: "sign-up-password-input",
            logInIdInput: "log-in-id-input",
            logInNameInput: "log-in-name-input",
            logInPasswordInput: "log-in-password-input",
            userNewNameInput: "user-new-name-input",
            userNewPasswordInput: "user-new-password-input",

        },

        TEXTLABELS:
        {

            userId: "user-id",
            userStatus: "user-status",
            userCurrentName: "user-current-name",
            userCurrentStatus: "user-current-status",
            userCurrentId: "user-current-id",
            profileInfo: "profile-info",

        },

    },

    TEXTCONSTANTS: 
    {

        userNotFoundAlertMessage: "Данного пользователя не существует, зарегистрируйтесь!",
        userName: "Имя: ",
        userStatus: "Статус: ",
        userId: "ID: ",
        successfullyUpdatedProfileMessage: "Профиль успешно обновлен!",
        userProfileDataArray: ["Имя: ", "Статус: ", "ID: "],

    },

    STATUS_CODES: 
    {

        success: "success",
        notAuthorized: "not_authorized",
        forbidden: "forbidden",

    },

}