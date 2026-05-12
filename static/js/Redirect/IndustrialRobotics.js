import { configRegistry } from "/static/js/config.js";
import { redirectToEndpoint } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const industrialRoboticsRedirectButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.industrialRoboticsRedirectButton);

    redirectToEndpoint({button: industrialRoboticsRedirectButton, endpoint: configRegistry.ENDPOINTS.industrialRoboticsEndpoint});
})