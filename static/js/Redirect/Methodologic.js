import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const methodologicRedirectButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.methodologicRedirectButton);

    redirectToEndpoint({button: methodologicRedirectButton, endpoint: configRegistry.ENDPOINTS.methodologicEndpoint})
})