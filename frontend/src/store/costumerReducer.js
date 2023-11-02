const defaultState = {
    costumers: []
  }
  
  export const costumerReducer = (state = defaultState, action) => {
    switch (action.type) {
      case "ADD_COSTUMER":
        return {...state, costumers: [...state.costumers, action.payload]}
  
        case "REMOVE_COSTUMER":
          return {
            ...state,
            costumers: state.costumers.filter((customer) => customer.id !== action.payload),
          };
        
      default:
        return state
    }
  }
  