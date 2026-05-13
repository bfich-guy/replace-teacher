import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const aboutRedirectButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.aboutRedirectButton);

    aboutRedirectButton.addEventListener("click", function() {
        redirectToEndpoint({endpoint: configRegistry.ENDPOINTS.aboutEndpoint});
    });

})