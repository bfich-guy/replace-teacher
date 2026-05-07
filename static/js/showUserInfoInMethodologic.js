import { configRegistry } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const userIdTextLabel = document.getElementById(configRegistry.WIDGETS.METHODOLOGIC_PAGE.TEXTLABELS.userId);
    const userStatusTextLabel = document.getElementById(configRegistry.WIDGETS.METHODOLOGIC_PAGE.TEXTLABELS.userStatus);

    const userId = localStorage.getItem(configRegistry.WIDGETS.METHODOLOGIC_PAGE.USER_INFO.userId);
    const userStatus = localStorage.getItem(configRegistry.WIDGETS.METHODOLOGIC_PAGE.USER_INFO.userStatus);

    userIdTextLabel.innerText = `ID: ${userId}`;
    userStatusTextLabel.innerText = `Статус: ${userStatus}`;
});