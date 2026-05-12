export const redirectToEndpoint = ({button, endpoint}) => {
    button.addEventListener("click", function() {
        window.location.href = endpoint
    });
}

export const parseUserData = ({userData}) => {
    const userName = userData?.name;
    const userStatus = userData?.status;
    const userId = userData?.unique_id;

    return [userName, userStatus, userId]
}