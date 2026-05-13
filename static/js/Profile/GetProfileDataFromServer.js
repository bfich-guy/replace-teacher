import { configRegistry } from "/static/js/config.js"
import { getUserNameStatusId, setInnerTextInTextlabel } from "/static/js/utils.js";

document.addEventListener("DOMContentLoaded", function() {

    const userCurrentName = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentName);
    const userCurrentStatus = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentStatus);
    const userCurrentId = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.userCurrentId);

    const profileInfo = document.getElementById(configRegistry.WIDGETS.TEXTLABELS.profileInfo);

    const userNewNameInput = document.getElementById(configRegistry.WIDGETS.INPUTS.userNewNameInput);
    const userNewPasswordInput = document.getElementById(configRegistry.WIDGETS.INPUTS.userNewPasswordInput);

    const profileUpdateButton = document.getElementById(configRegistry.WIDGETS.BUTTONS.profileUpdateButton);
    
    profileUpdateButton.addEventListener("click", function() {

        const userNewNameInputValue = userNewNameInput.value;
        const userNewPasswordInputValue = userNewPasswordInput.value;

        fetch(configRegistry.ENDPOINTS.updateProfileEndpoint, 
        {

            headers: configRegistry.HEADERS.contentTypeApplicationJSON,
            method: configRegistry.METHODS.GET,
        })
        .then(response => response.json())
        .then(responseData => {

            if (responseData.status === configRegistry.STATUS_CODES.notAuthorized)
            {
                profileInfo.innerText = configRegistry.TEXTCONSTANTS.userNotFoundAlertMessage;
            }

            const userDataArray = getUserNameStatusId({userData: responseData});
            const textlabelArray = [userCurrentName, userCurrentStatus, userCurrentId];

            setInnerTextInTextlabel({textlabelArray: textlabelArray, innerTextlabelArray: userDataArray, extraLeftTextlabelArray: configRegistry.TEXTCONSTANTS.userProfileDataArray}); 

        })

        profileInfo.innerText = configRegistry.TEXTCONSTANTS.successfullyUpdatedProfileMessage;
    })
})