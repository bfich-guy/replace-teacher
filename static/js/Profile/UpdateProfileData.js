import { configRegistry } from "/static/js/config.js";
import { getUserNameStatusId, setInnerTextInTextlabel } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const userCurrentName = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentName);
    const userCurrentStatus = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentStatus);
    const userCurrentId = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentId);

    fetch(configRegistry.ENDPOINTS.updateProfileEndpoint, {

        headers: configRegistry.HEADERS.contentTypeApplicationJSON,
        method: configRegistry.METHODS.GET

    })
    .then(response => response.json())
    .then(responseData => {

        const userDataArray = getUserNameStatusId({userData: responseData});

        console.log(userDataArray);

        const textlabelArray = [userCurrentName, userCurrentStatus, userCurrentId];

        setInnerTextInTextlabel({textlabelArray: textlabelArray, innerTextlabelArray: userDataArray, extraLeftTextlabelArray: configRegistry.TEXTCONSTANTS.userProfileDataArray});

    });
    
});