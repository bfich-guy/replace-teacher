import { configRegistry } from "/static/js/config.js"

document.addEventListener("DOMContentLoaded", function() {

    const userCurrentName = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentName);
    const userCurrentStatus = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentStatus);
    const userCurrentId = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentId);

    const userNewNameInput = document.getElementById(configRegistry.WIDGETS.INPUTS.userNewNameInput);
    const userNewPasswordInput = document.getElementById(configRegistry.WIDGETS.INPUTS.userNewPasswordInput);

    const profileUpdateButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.profileUpdateButton);
    
    profileUpdateButton.addEventListener("click", function() {

        const userNewNameInputValue = userNewNameInput.value;
        const userNewPasswordInputValue = userNewPasswordInput.value;

        fetch(configRegistry.ENDPOINTS.updateProfileEndpoint, 
        {

            headers: configRegistry.HEADERS.contentTypeApplicationJSON,
            method: configRegistry.METHODS.POST,
            body: JSON.stringify({
                new_user_name: userNewNameInputValue,
                new_user_password: userNewPasswordInputValue,
            })

        });
    });
});