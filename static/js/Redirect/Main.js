import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const mainRedirectButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.mainRedirectButton);

    mainRedirectButton.addEventListener("click", function() {
        redirectToEndpoint({endpoint: configRegistry.ENDPOINTS.aboutEndpoint});
    });

})