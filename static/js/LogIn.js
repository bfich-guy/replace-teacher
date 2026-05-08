import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const logInIdInput = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.logInIdInput);
    const logInNameInput = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.logInNameInput);
    const logInPasswordInput = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.INPUTS.logInPasswordInput);

    const logInButton = document.getElementById(configRegistry.WIDGETS.INDEX_PAGE.BUTTONS.logInButton);

    logInButton.addEventListener("click", function() {

        const logInIdValue = logInIdInput.value;
        const logInNameValue = logInNameInput.value;
        const logInPasswordValue = logInPasswordInput.value;

        const logInDataIsNotNull = (logInIdValue && logInNameValue && logInPasswordValue)

        if (logInDataIsNotNull) 
        {
            fetch(configRegistry.ENDPOINTS.logInEndpoint, 
            {
                headers: configRegistry.HEADERS.contentTypeApplicationJSON,
                method: configRegistry.METHODS.POST,
                body: JSON.stringify({
                    auth_type: configRegistry.AUTH.TYPE.log_in,
                    file_path: configRegistry.DATABASE.users,
                    user_input_data: {
                        name: logInNameValue || null,
                        password: logInPasswordValue || null,
                        status: null,
                        unique_id: logInIdValue,
                    }
                })
            })
            .then(response => response.json())
            .then(responseData => {

                const statusCodeIsSuccess = responseData.status === "success"; //Hardcode

                if (statusCodeIsSuccess) 
                {
                    window.location.href = configRegistry.ENDPOINTS.methodologicEndpoint;
                }
                else
                {
                    alert("ТЫ КТО ВООБЩЕ ТАКОЙ?!");
                };

            });
        };
    });
});