import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const logInIdInput = document.getElementById(configRegistry.WIDGETS.INPUTS.logInIdInput);
    const logInNameInput = document.getElementById(configRegistry.WIDGETS.INPUTS.logInNameInput);
    const logInPasswordInput = document.getElementById(configRegistry.WIDGETS.INPUTS.logInPasswordInput);

    const logInButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.logInButton);

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
                    user_input_data: {
                        name: logInNameValue || null,
                        password: logInPasswordValue || null,
                        status: null,
                        unique_id: logInIdValue || null,
                    }
                })
            })
            .then(response => response.json())
            .then(responseData => {

                const statusCodeIsSuccess = responseData.status === configRegistry.STATUS_CODES.success;

                if (statusCodeIsSuccess) 
                {
                    redirectToEndpoint({endpoint: configRegistry.ENDPOINTS.mainEndpoint});
                    //window.location.href = configRegistry.ENDPOINTS.mainEndpoint;
                }
                else
                {
                    alert(configRegistry.TEXTCONSTANTS.userNotFoundAlertMessage);
                };

            });
        };
    });
});