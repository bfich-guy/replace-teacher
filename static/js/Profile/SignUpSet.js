import { configRegistry } from "/static/js/config.js";
import { parseUserData } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const userCurrentName = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentName);
    const userCurrentStatus = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentStatus);
    const userCurrentId = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentId);

    fetch(configRegistry.ENDPOINTS.signUpEndpoint, {
        headers: configRegistry.HEADERS.contentTypeApplicationJSON,
        method: configRegistry.METHODS.GET,
    })
    .then(responce => responce.json())
    .then(userData => {

        const [userName, userStatus, userId] = parseUserData({userData});

        userCurrentName.innerText = `${configRegistry.TEXTCONSTANTS.userName}${userName}`;
        userCurrentStatus.innerText = `${configRegistry.TEXTCONSTANTS.userStatus}${userStatus}`;
        userCurrentId.innerText = `${configRegistry.TEXTCONSTANTS.userId}${userId}`;

    })
})