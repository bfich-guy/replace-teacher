import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const industrialRoboticsRedirectButton = document.getElementById(configRegistry.WIDGETS.METHODOLOGIC_PAGE.BUTTONS.industrialRoboticsRedirectButton);

    industrialRoboticsRedirectButton.addEventListener("click", function() {

        window.location.href = configRegistry.ENDPOINTS.industrialRoboticsEndpoint;

    })
})