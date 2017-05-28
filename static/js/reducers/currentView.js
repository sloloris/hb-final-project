// creates constant function currentView, initializes state to default view index 0, passes all actions from index.js

const currentView = (state = 0, action) => {
    switch(action.type) {
        case 'SET_CURRENT_VIEW':
            // returns action.payload.index for setCurrentView action from index.js
            return action.payload.index

        default: 
            return state // whatever value state is on
    }
}

export default currentView