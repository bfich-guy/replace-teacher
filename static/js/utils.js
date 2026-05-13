export const redirectToEndpoint = ({endpoint}) => {
    window.location.href = endpoint
}


/**  This function **returns name, status and ID** of User. */
export const getUserNameStatusId = ({userData}) => {
    
    const userName = userData?.name;
    const userStatus = userData?.status;
    const userId = userData?.unique_id;

    return [userName, userStatus, userId]
}

/**  This function **gets text labels array and inner texts array** for this labels and **sets the inner text into each textlabel in array**. */
export const setInnerTextInTextlabel = ({textlabelArray, innerTextlabelArray, extraLeftTextlabelArray}) => {

    const textlabelArrayLength = textlabelArray.length;
    const innerTextlabelArrayLength = innerTextlabelArray.length;

    const hasLengthMismatch = (textlabelArrayLength !== innerTextlabelArrayLength);

    if (hasLengthMismatch)
    {
        return null;
    }
    else
    {
        for(let textLabelIndex = 0; textLabelIndex < textlabelArrayLength; textLabelIndex++)
        {
            const textLabel = textlabelArray[textLabelIndex]
            textLabel.innerText = extraLeftTextlabelArray[textLabelIndex] + innerTextlabelArray[textLabelIndex]
        }

        return null;
    }
}