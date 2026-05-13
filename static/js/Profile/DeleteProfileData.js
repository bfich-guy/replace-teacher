import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const profileDeleteButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.profileDeleteButton);

    profileDeleteButton.addEventListener("click", function() 
    {

        fetch(configRegistry.ENDPOINTS.deleteProfileEndpoint, 
        {

            headers: configRegistry.HEADERS.contentTypeApplicationJSON,
            method: configRegistry.METHODS.GET,

        });

        redirectToEndpoint({endpoint: configRegistry.ENDPOINTS.mainEndpoint});

    });
});