import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const profileRedirectButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.profileRedirectButton);

    redirectToEndpoint({button: profileRedirectButton, endpoint: configRegistry.ENDPOINTS.profileEndpoint})
})