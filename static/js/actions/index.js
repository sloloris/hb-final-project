// defines 'action creators', or what reducers listen to

export const setCurrentView = (index) => ({
    type: 'SET_CURRENT_VIEW',
    payload: {
        index: index
    }
})

export const logoutUser = () => {
    console.log('use theoretically logs out here')
}